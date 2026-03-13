import json
import uuid
from typing import Dict, List, Any, Optional, Tuple

try:
    from .moyin_types import (
        AIScene, AICharacter, AIScreenplay, GenerationConfig,
        CharacterBible, SceneStatus, CameraType
    )
    from .prompt_compiler import PromptCompiler, prompt_compiler
    from .character_bible import (
        CharacterBibleManager, character_bible_manager,
        generate_consistency_prompt, merge_character_analyses
    )
except ImportError:
    from moyin_types import (
        AIScene, AICharacter, AIScreenplay, GenerationConfig,
        CharacterBible, SceneStatus, CameraType
    )
    from prompt_compiler import PromptCompiler, prompt_compiler
    from character_bible import (
        CharacterBibleManager, character_bible_manager,
        generate_consistency_prompt, merge_character_analyses
    )


class MoyinPromptCompilerNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "template_type": (["scene_image", "scene_video", "screenplay", "negative"],),
            },
            "optional": {
                "style_tokens": ("STRING", {"default": "", "multiline": True}),
                "quality_tokens": ("STRING", {"default": "", "multiline": True}),
                "character_description": ("STRING", {"default": "", "multiline": True}),
                "visual_content": ("STRING", {"default": "", "multiline": True}),
                "camera": (["Close-up", "Medium Shot", "Wide Shot", "Two-Shot", "Over-the-shoulder", "Tracking", "POV", "Low Angle", "High Angle", "Profile Shot", "Dutch Angle"],),
                "action": ("STRING", {"default": "", "multiline": True}),
                "user_prompt": ("STRING", {"default": "", "multiline": True}),
                "scene_count": ("INT", {"default": 5, "min": 1, "max": 50}),
                "additional_negative_terms": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("compiled_prompt",)
    FUNCTION = "compile_prompt"
    CATEGORY = "Moyin Creator"
    
    def compile_prompt(
        self,
        template_type: str,
        style_tokens: str = "",
        quality_tokens: str = "",
        character_description: str = "",
        visual_content: str = "",
        camera: str = "Medium Shot",
        action: str = "",
        user_prompt: str = "",
        scene_count: int = 5,
        additional_negative_terms: str = "",
    ) -> Tuple[str]:
        variables = {}
        
        if style_tokens:
            variables["style_tokens"] = style_tokens
        if quality_tokens:
            variables["quality_tokens"] = quality_tokens
        if character_description:
            variables["character_description"] = character_description
        if visual_content:
            variables["visual_content"] = visual_content
        if camera:
            variables["camera"] = camera
        if action:
            variables["action"] = action
        if user_prompt:
            variables["prompt"] = user_prompt
        if scene_count:
            variables["scene_count"] = str(scene_count)
        
        if template_type == "negative":
            terms = [t.strip() for t in additional_negative_terms.split(",") if t.strip()]
            result = prompt_compiler.get_negative_prompt(terms)
        elif template_type == "screenplay":
            result = prompt_compiler.compile_screenplay_prompt(user_prompt, scene_count)
        elif template_type == "scene_image":
            result = prompt_compiler.compile("scene_image", variables)
        elif template_type == "scene_video":
            result = prompt_compiler.compile("scene_video", variables)
        else:
            result = ""
        
        return (result,)


class MoyinCharacterBibleNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "operation": (["add_character", "get_character", "build_prompt", "build_style_tokens", "export_all", "clear"],),
            },
            "optional": {
                "character_name": ("STRING", {"default": "Character"}),
                "character_type": (["human", "cat", "dog", "rabbit", "bear", "bird", "other"],),
                "visual_traits": ("STRING", {"default": "", "multiline": True}),
                "style_tokens_str": ("STRING", {"default": "", "multiline": True}),
                "personality": ("STRING", {"default": "", "multiline": True}),
                "character_id": ("STRING", {"default": ""}),
                "character_ids_str": ("STRING", {"default": "", "multiline": True}),
                "screenplay_id": ("STRING", {"default": ""}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("result", "character_id")
    FUNCTION = "manage_character"
    CATEGORY = "Moyin Creator"
    
    def manage_character(
        self,
        operation: str,
        character_name: str = "Character",
        character_type: str = "human",
        visual_traits: str = "",
        style_tokens_str: str = "",
        personality: str = "",
        character_id: str = "",
        character_ids_str: str = "",
        screenplay_id: str = "",
    ) -> Tuple[str, str]:
        result_id = ""
        
        if operation == "add_character":
            style_tokens = [t.strip() for t in style_tokens_str.split(",") if t.strip()]
            char = character_bible_manager.add_character({
                "name": character_name,
                "type": character_type,
                "visual_traits": visual_traits,
                "style_tokens": style_tokens,
                "personality": personality,
                "screenplay_id": screenplay_id,
            })
            result = json.dumps({
                "id": char.id,
                "name": char.name,
                "type": char.type,
                "visual_traits": char.visual_traits,
            }, ensure_ascii=False, indent=2)
            result_id = char.id
        
        elif operation == "get_character":
            char = character_bible_manager.get_character(character_id)
            if char:
                result = json.dumps({
                    "id": char.id,
                    "name": char.name,
                    "type": char.type,
                    "visual_traits": char.visual_traits,
                    "style_tokens": char.style_tokens,
                    "personality": char.personality,
                }, ensure_ascii=False, indent=2)
                result_id = char.id
            else:
                result = "Character not found"
        
        elif operation == "build_prompt":
            char_ids = [cid.strip() for cid in character_ids_str.split(",") if cid.strip()]
            result = character_bible_manager.build_character_prompt(char_ids)
        
        elif operation == "build_style_tokens":
            char_ids = [cid.strip() for cid in character_ids_str.split(",") if cid.strip()]
            tokens = character_bible_manager.build_style_tokens(char_ids)
            result = ", ".join(tokens)
        
        elif operation == "export_all":
            chars = character_bible_manager.export_all()
            result = json.dumps(chars, ensure_ascii=False, indent=2)
        
        elif operation == "clear":
            character_bible_manager.clear()
            result = "All characters cleared"
        
        else:
            result = "Unknown operation"
        
        return (result, result_id)


class MoyinSceneGeneratorNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scene_id": ("INT", {"default": 1, "min": 1}),
                "narration": ("STRING", {"default": "", "multiline": True}),
            },
            "optional": {
                "visual_content": ("STRING", {"default": "", "multiline": True}),
                "action": ("STRING", {"default": "", "multiline": True}),
                "camera": (["Close-up", "Medium Shot", "Wide Shot", "Two-Shot", "Over-the-shoulder", "Tracking", "POV", "Low Angle", "High Angle", "Profile Shot", "Dutch Angle"],),
                "character_description": ("STRING", {"default": "", "multiline": True}),
                "mood": ("STRING", {"default": ""}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("scene_json",)
    FUNCTION = "generate_scene"
    CATEGORY = "Moyin Creator"
    
    def generate_scene(
        self,
        scene_id: int,
        narration: str,
        visual_content: str = "",
        action: str = "",
        camera: str = "Medium Shot",
        character_description: str = "",
        mood: str = "",
    ) -> Tuple[str]:
        scene = {
            "scene_id": scene_id,
            "narration": narration,
            "visual_content": visual_content,
            "action": action,
            "camera": camera,
            "character_description": character_description,
            "mood": mood,
            "status": "pending",
        }
        return (json.dumps(scene, ensure_ascii=False, indent=2),)


class MoyinScreenplayGeneratorNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "title": ("STRING", {"default": "My Video"}),
            },
            "optional": {
                "genre": ("STRING", {"default": ""}),
                "aspect_ratio": (["16:9", "9:16"],),
                "scenes_json": ("STRING", {"default": "[]", "multiline": True}),
                "characters_json": ("STRING", {"default": "[]", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("screenplay_json",)
    FUNCTION = "generate_screenplay"
    CATEGORY = "Moyin Creator"
    
    def generate_screenplay(
        self,
        title: str,
        genre: str = "",
        aspect_ratio: str = "16:9",
        scenes_json: str = "[]",
        characters_json: str = "[]",
    ) -> Tuple[str]:
        try:
            scenes = json.loads(scenes_json)
        except:
            scenes = []
        
        try:
            characters = json.loads(characters_json)
        except:
            characters = []
        
        screenplay = {
            "id": str(uuid.uuid4()),
            "title": title,
            "genre": genre,
            "aspect_ratio": aspect_ratio,
            "orientation": "landscape" if aspect_ratio == "16:9" else "portrait",
            "characters": characters,
            "scenes": scenes,
        }
        return (json.dumps(screenplay, ensure_ascii=False, indent=2),)


class MoyinConsistencyPromptNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "character_bible_json": ("STRING", {"default": "", "multiline": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("consistency_prompt",)
    FUNCTION = "generate_consistency"
    CATEGORY = "Moyin Creator"
    
    def generate_consistency(self, character_bible_json: str) -> Tuple[str]:
        try:
            char_data = json.loads(character_bible_json)
            visual_traits = char_data.get("visual_traits", "")
            style_tokens = char_data.get("style_tokens", [])
            name = char_data.get("name", "Character")
            
            parts = []
            if visual_traits:
                parts.append(visual_traits)
            if style_tokens:
                parts.append(", ".join(style_tokens))
            parts.append(f"character: {name}")
            
            return (", ".join(parts),)
        except:
            return ("",)
