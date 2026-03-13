# ComfyUI Moyin Creator Nodes

将魔因漫创 (Moyin Creator) 的核心功能转换为 ComfyUI 自定义节点。

## 功能特性

### 1. Moyin Prompt Compiler (提示词编译器)
- 支持场景图像提示词生成
- 支持场景视频提示词生成
- 支持剧本创作提示词生成
- 支持负面提示词生成

### 2. Moyin Character Bible (角色圣经管理器)
- 添加角色
- 获取角色信息
- 构建角色一致性提示词
- 构建角色风格标记
- 导出/导入所有角色

### 3. Moyin Scene Generator (场景生成器)
- 创建单个场景
- 支持旁白、视觉内容、动作、镜头类型等参数

### 4. Moyin Screenplay Generator (剧本生成器)
- 创建完整剧本
- 支持多个场景和角色
- 支持 16:9 和 9:16 两种宽高比

### 5. Moyin Consistency Prompt (一致性提示词生成器)
- 从角色圣经数据生成一致性提示词

## 安装方法

1. 将 `comfyui-moyin-nodes` 文件夹复制到 ComfyUI 的 `custom_nodes` 目录下：
   ```
   ComfyUI/
   └── custom_nodes/
       └── comfyui-moyin-nodes/
           ├── __init__.py
           ├── nodes.py
           ├── types.py
           ├── prompt_compiler.py
           ├── character_bible.py
           └── README.md
   ```

2. 重启 ComfyUI

## 使用说明

### 基本工作流

1. **创建角色**
   - 使用 `Moyin Character Bible` 节点，选择 `add_character` 操作
   - 输入角色名称、类型、视觉特征、风格标记等信息

2. **创建场景**
   - 使用 `Moyin Scene Generator` 节点创建单个场景
   - 可以创建多个场景并使用自定义节点组合成场景列表

3. **创建剧本**
   - 使用 `Moyin Screenplay Generator` 节点
   - 输入场景 JSON 数组和角色 JSON 数组

4. **生成提示词**
   - 使用 `Moyin Prompt Compiler` 节点
   - 选择模板类型，输入相应参数
   - 生成图像或视频提示词

5. **角色一致性**
   - 使用 `Moyin Consistency Prompt` 节点
   - 输入角色圣经 JSON 数据
   - 生成一致性提示词用于图像生成

## 节点详细说明

### Moyin Prompt Compiler

**输入参数：**
- `template_type`: 模板类型
  - `scene_image`: 场景图像提示词
  - `scene_video`: 场景视频提示词
  - `screenplay`: 剧本创作提示词
  - `negative`: 负面提示词
- `style_tokens`: 风格标记（逗号分隔）
- `quality_tokens`: 质量标记（逗号分隔）
- `character_description`: 角色描述
- `visual_content`: 视觉内容
- `camera`: 镜头类型
- `action`: 动作描述
- `user_prompt`: 用户提示词（用于剧本生成）
- `scene_count`: 场景数量
- `additional_negative_terms`: 额外负面词（逗号分隔）

**输出：**
- `compiled_prompt`: 编译后的提示词

### Moyin Character Bible

**输入参数：**
- `operation`: 操作类型
  - `add_character`: 添加角色
  - `get_character`: 获取角色
  - `build_prompt`: 构建角色提示词
  - `build_style_tokens`: 构建风格标记
  - `export_all`: 导出所有角色
  - `clear`: 清空所有角色
- `character_name`: 角色名称
- `character_type`: 角色类型
- `visual_traits`: 视觉特征
- `style_tokens_str`: 风格标记（逗号分隔）
- `personality`: 性格描述
- `character_id`: 角色ID
- `character_ids_str`: 角色ID列表（逗号分隔）
- `screenplay_id`: 剧本ID

**输出：**
- `result`: 操作结果（JSON或字符串）
- `character_id`: 角色ID

### Moyin Scene Generator

**输入参数：**
- `scene_id`: 场景ID
- `narration`: 旁白
- `visual_content`: 视觉内容
- `action`: 动作
- `camera`: 镜头类型
- `character_description`: 角色描述
- `mood`: 情绪

**输出：**
- `scene_json`: 场景JSON

### Moyin Screenplay Generator

**输入参数：**
- `title`: 标题
- `genre`: 类型
- `aspect_ratio`: 宽高比
- `scenes_json`: 场景JSON数组
- `characters_json`: 角色JSON数组

**输出：**
- `screenplay_json`: 剧本JSON

### Moyin Consistency Prompt

**输入参数：**
- `character_bible_json`: 角色圣经JSON

**输出：**
- `consistency_prompt`: 一致性提示词

## 示例工作流

项目包含一个预配置的示例工作流文件 `example_workflow.json`，可以直接拖拽到 ComfyUI 中使用。

### 示例工作流包含：
- 2 个角色创建节点（Alice 和 Bob）
- 2 个场景生成节点（樱花公园相遇场景）
- 2 个提示词编译器节点（场景图像和负面提示词）
- 1 个一致性提示词生成节点
- 1 个剧本生成器节点
- 1 个说明注释节点

### 使用方法：
1. 在 ComfyUI 中点击「Load」按钮，或直接将 `example_workflow.json` 文件拖拽到 ComfyUI 界面
2. 根据需要修改节点参数
3. 连接到其他 ComfyUI 节点（如 KSampler、CLIP Text Encode 等）进行图像/视频生成

## 许可证

本项目采用 AGPL-3.0 许可证开源，与原始 moyin-creator 项目保持一致。
