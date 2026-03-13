from nodes import (
    MoyinPromptCompilerNode,
    MoyinCharacterBibleNode,
    MoyinSceneGeneratorNode,
    MoyinScreenplayGeneratorNode,
    MoyinConsistencyPromptNode,
)

NODE_CLASS_MAPPINGS = {
    "MoyinPromptCompiler": MoyinPromptCompilerNode,
    "MoyinCharacterBible": MoyinCharacterBibleNode,
    "MoyinSceneGenerator": MoyinSceneGeneratorNode,
    "MoyinScreenplayGenerator": MoyinScreenplayGeneratorNode,
    "MoyinConsistencyPrompt": MoyinConsistencyPromptNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MoyinPromptCompiler": "Moyin Prompt Compiler",
    "MoyinCharacterBible": "Moyin Character Bible",
    "MoyinSceneGenerator": "Moyin Scene Generator",
    "MoyinScreenplayGenerator": "Moyin Screenplay Generator",
    "MoyinConsistencyPrompt": "Moyin Consistency Prompt",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
