from nodes import (
    MoyinCreateCharacter,
    MoyinCharacterToPrompt,
    MoyinCreateScene,
    MoyinBuildImagePrompt,
    MoyinBuildVideoPrompt,
    MoyinBuildNegativePrompt,
    MoyinCombineScenes,
    MoyinCreateScreenplay,
    MoyinSceneToImagePrompt,
    MoyinAPIConfig,
)

NODE_CLASS_MAPPINGS = {
    "MoyinCreateCharacter": MoyinCreateCharacter,
    "MoyinCharacterToPrompt": MoyinCharacterToPrompt,
    "MoyinCreateScene": MoyinCreateScene,
    "MoyinBuildImagePrompt": MoyinBuildImagePrompt,
    "MoyinBuildVideoPrompt": MoyinBuildVideoPrompt,
    "MoyinBuildNegativePrompt": MoyinBuildNegativePrompt,
    "MoyinCombineScenes": MoyinCombineScenes,
    "MoyinCreateScreenplay": MoyinCreateScreenplay,
    "MoyinSceneToImagePrompt": MoyinSceneToImagePrompt,
    "MoyinAPIConfig": MoyinAPIConfig,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MoyinCreateCharacter": "🪄 Create Character",
    "MoyinCharacterToPrompt": "✨ Character to Prompt",
    "MoyinCreateScene": "🎬 Create Scene",
    "MoyinBuildImagePrompt": "🖼️ Build Image Prompt",
    "MoyinBuildVideoPrompt": "🎥 Build Video Prompt",
    "MoyinBuildNegativePrompt": "🚫 Build Negative Prompt",
    "MoyinCombineScenes": "📚 Combine Scenes",
    "MoyinCreateScreenplay": "📖 Create Screenplay",
    "MoyinSceneToImagePrompt": "🎨 Scene to Image Prompt",
    "MoyinAPIConfig": "🔧 API Config",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
