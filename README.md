# ComfyUI Moyin Creator Nodes

将魔因漫创 (Moyin Creator) 的核心功能转换为 ComfyUI 自定义节点。

## 功能特性

节点按功能分组，使用更简单清晰：

### 👤 Character (角色)
- **🪄 Create Character** - 创建角色
- **✨ Character to Prompt** - 角色转提示词

### 🎬 Scene (场景)
- **🎬 Create Scene** - 创建场景
- **📚 Combine Scenes** - 组合场景

### ✨ Prompt (提示词)
- **🖼️ Build Image Prompt** - 构建图像提示词
- **🎥 Build Video Prompt** - 构建视频提示词
- **🚫 Build Negative Prompt** - 构建负面提示词
- **🎨 Scene to Image Prompt** - 场景转图像提示词

### 📖 Screenplay (剧本)
- **📖 Create Screenplay** - 创建剧本

## 安装方法

### 方法 1: 手动安装（推荐）

1. 将 `comfyui-moyin-nodes` 文件夹复制到 ComfyUI 的 `custom_nodes` 目录下：
   ```
   ComfyUI/
   └── custom_nodes/
       └── comfyui-moyin-nodes/
           ├── __init__.py
           ├── nodes.py
           ├── moyin_types.py
           ├── prompt_compiler.py
           ├── character_bible.py
           ├── example_workflow.json
           └── README.md
   ```

2. **重启 ComfyUI**（必须完全重启，不是刷新页面）

3. 在 ComfyUI 中搜索节点：
   - 右键点击画布 → Add Node → Moyin Creator
   - 或直接在搜索框输入 "Moyin" 或节点名称

### 方法 2: Git 安装

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yangezhang03-jpg/-.git comfyui-moyin-nodes
```

然后重启 ComfyUI。

## 常见问题

### 搜索不到节点？

1. **确认文件夹位置正确**：必须在 `ComfyUI/custom_nodes/comfyui-moyin-nodes/` 下
2. **确认已重启 ComfyUI**：不是刷新浏览器，是完全关闭再打开
3. **检查 ComfyUI 控制台**：看是否有错误信息
4. **确认文件名**：`moyin_types.py`（不是 `types.py`）

### 节点在哪里？

节点在以下分组中：
- `Moyin Creator/Character` - 角色相关节点
- `Moyin Creator/Scene` - 场景相关节点
- `Moyin Creator/Prompt` - 提示词相关节点
- `Moyin Creator/Screenplay` - 剧本相关节点

或者直接搜索：
- "Create Character"
- "Create Scene"
- "Build Image Prompt"
- 等等...

## 使用说明

### 快速开始

1. 将 `example_workflow.json` 拖拽到 ComfyUI 中
2. 查看示例工作流
3. 根据需要修改参数
4. 连接到 CLIP、KSampler、VAE 等节点生成图像

### 基本工作流

#### 1. 创建角色

```
🪄 Create Character → ✨ Character to Prompt
     ↓
   (character_json) → (character_prompt)
```

**Create Character 参数：**
- `name`: 角色名称
- `character_type`: 角色类型（human/cat/dog等）
- `visual_traits`: 视觉特征（如：blonde hair, blue eyes）
- `style_tokens`: 风格标记（如：anime style）
- `personality`: 性格描述

**Character to Prompt：**
- 输入：character_json
- 输出：character_prompt（可直接用于图像生成）

#### 2. 创建场景

```
🎬 Create Scene → 🎨 Scene to Image Prompt
     ↓                    ↓
  (scene_json)      (image_prompt)
```

**Create Scene 参数：**
- `scene_id`: 场景编号
- `narration`: 中文旁白
- `visual_content`: 英文视觉描述
- `action`: 角色动作
- `camera`: 镜头类型
- `character_description`: 角色外观
- `mood`: 情绪

**Scene to Image Prompt：**
- 输入：scene_json, character_prompt, style_tokens 等
- 输出：完整的 image_prompt

#### 3. 生成提示词

```
🚫 Build Negative Prompt
     ↓
  (negative_prompt)
```

**Build Negative Prompt：**
- 输入：additional_terms（额外负面词）
- 输出：negative_prompt

#### 4. 连接到 ComfyUI

```
image_prompt → CLIP Text Encode (Prompt)
negative_prompt → CLIP Text Encode (Negative Prompt)
                     ↓
                  KSampler
                     ↓
                  VAE Decode
                     ↓
                  Save Image
```

## 节点详细说明

### 🪄 Create Character

**分类：** `Moyin Creator/Character`

**输入：**
- `name`: 角色名称
- `character_type`: 角色类型（human/cat/dog/rabbit/bear/bird/other）
- `visual_traits`: 视觉特征（多行文本）
- `style_tokens`: 风格标记（可选，多行）
- `personality`: 性格（可选，多行）
- `screenplay_id`: 剧本ID（可选）

**输出：**
- `character_json`: 角色 JSON 数据
- `character_id`: 角色 ID

### ✨ Character to Prompt

**分类：** `Moyin Creator/Character`

**输入：**
- `character_json`: 角色 JSON 数据

**输出：**
- `character_prompt`: 角色提示词字符串

### 🎬 Create Scene

**分类：** `Moyin Creator/Scene`

**输入：**
- `scene_id`: 场景编号
- `narration`: 中文旁白（多行）
- `visual_content`: 英文视觉描述（可选，多行）
- `action`: 角色动作（可选，多行）
- `camera`: 镜头类型
- `character_description`: 角色外观（可选，多行）
- `mood`: 情绪（可选）

**输出：**
- `scene_json`: 场景 JSON 数据

### 📚 Combine Scenes

**分类：** `Moyin Creator/Scene`

**输入：**
- `scene_1` 到 `scene_5`: 场景 JSON（可选）

**输出：**
- `scenes_json`: 场景数组 JSON

### 🖼️ Build Image Prompt

**分类：** `Moyin Creator/Prompt`

**输入：**
- `style_tokens`: 风格标记（可选）
- `character_prompt`: 角色提示词（可选）
- `visual_content`: 视觉内容（可选）
- `camera`: 镜头类型
- `quality_tokens`: 质量标记

**输出：**
- `image_prompt`: 图像提示词

### 🎥 Build Video Prompt

**分类：** `Moyin Creator/Prompt`

**输入：**
- `character_prompt`: 角色提示词（可选）
- `visual_content`: 视觉内容（可选）
- `action`: 动作描述（可选）
- `camera`: 镜头类型

**输出：**
- `video_prompt`: 视频提示词

### 🚫 Build Negative Prompt

**分类：** `Moyin Creator/Prompt`

**输入：**
- `additional_terms`: 额外负面词（可选，多行）

**输出：**
- `negative_prompt`: 负面提示词

### 🎨 Scene to Image Prompt

**分类：** `Moyin Creator/Prompt`

**输入：**
- `scene_json`: 场景 JSON
- `style_tokens`: 风格标记（可选）
- `character_prompt`: 角色提示词（可选）
- `quality_tokens`: 质量标记

**输出：**
- `image_prompt`: 图像提示词

### 📖 Create Screenplay

**分类：** `Moyin Creator/Screenplay`

**输入：**
- `title`: 标题
- `genre`: 类型（可选）
- `aspect_ratio`: 宽高比（16:9/9:16）
- `scenes_json`: 场景 JSON 数组（可选）

**输出：**
- `screenplay_json`: 剧本 JSON

## 示例工作流

项目包含一个预配置的示例工作流文件 `example_workflow.json`，可以直接拖拽到 ComfyUI 中使用。

### 示例工作流包含：
- 2 个角色创建（Alice 和 Bob）
- 2 个场景创建（樱花公园相遇）
- 2 个场景转图像提示词
- 1 个负面提示词生成
- 详细的说明注释

### 使用方法：
1. 在 ComfyUI 中直接将 `example_workflow.json` 文件拖拽到界面
2. 或点击「Load」按钮加载文件
3. 根据需要修改节点参数
4. 将 image_prompt 和 negative_prompt 连接到 CLIP Text Encode 节点
5. 连接到 KSampler、VAE Decode、Save Image 等节点
6. 点击「Queue Prompt」生成图像！

## 项目结构

```
comfyui-moyin-nodes/
├── __init__.py              # 节点注册文件
├── nodes.py                 # 节点定义
├── moyin_types.py           # 数据类型定义
├── prompt_compiler.py       # 提示词编译器
├── character_bible.py       # 角色圣经管理器
├── example_workflow.json    # 示例工作流
├── test_nodes.py            # 测试脚本
├── test_import.py           # 导入测试
├── README.md                # 本文件
└── .gitignore               # Git 忽略文件
```

## 许可证

本项目采用 AGPL-3.0 许可证开源，与原始 moyin-creator 项目保持一致。
