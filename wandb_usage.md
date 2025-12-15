# Wandb 使用指南（远程公共PC）

本文档说明如何在远程公共PC上使用 Wandb，确保不影响其他用户。

## 快速开始

### 1. 获取 Wandb API Key

1. 访问 https://wandb.ai/settings
2. 在 "API keys" 部分，复制你的 API key
3. 如果还没有 API key，点击 "Create" 创建一个

### 2. 配置 Wandb

编辑配置文件并填入你的 API Key：

```bash
# 编辑配置文件
nano /home/kemove/qyh/lerobot/wandb_config.sh
# 或使用 vim
vim /home/kemove/qyh/lerobot/wandb_config.sh
```

在文件中找到 `export WANDB_API_KEY=""` 这一行，将你的 API Key 填入引号内：

```bash
export WANDB_API_KEY="your_api_key_here"
```

### 3. 配置 Entity（若使用组织）

若你在组织下（如 SJTU），`WANDB_ENTITY` 需要使用 “用户名-组织” 形式。例如：

```bash
export WANDB_ENTITY="qiuyuhao19990704-sjtu"
```

### 4. 加载配置

每次使用 Wandb 前，加载配置文件：

```bash
source /home/kemove/qyh/lerobot/wandb_config.sh
```

或者将其添加到你的 shell 配置文件（`~/.bashrc` 或 `~/.zshrc`）中：

```bash
# 添加到 ~/.zshrc 或 ~/.bashrc
echo "source /home/kemove/qyh/lerobot/wandb_config.sh" >> ~/.zshrc
```

## 使用方式

### 方式一：使用环境变量配置（推荐）

1. 加载配置：
```bash
source /home/kemove/qyh/lerobot/wandb_config.sh
```

2. 运行训练（Wandb 会自动使用环境变量中的配置）：
```bash
lerobot-train \
    --wandb.enable=true \
    --wandb.project=lerobot \
    --wandb.entity=qiuyuhao19990704-sjtu \
    # ... 其他参数
```

### 方式二：在训练命令中直接指定

如果不想使用环境变量，可以在训练命令中直接指定：

```bash
lerobot-train \
    --wandb.enable=true \
    --wandb.project=lerobot \
    --wandb.mode=online \
    --wandb.entity=qiuyuhao19990704-sjtu \
    # ... 其他参数
```

### 方式三：离线模式（网络不稳定时）

如果网络不稳定或无法连接 Wandb 服务器，使用离线模式：

```bash
# 方法1: 修改配置文件中的 WANDB_MODE
export WANDB_MODE="offline"

# 方法2: 在训练命令中指定
lerobot-train \
    --wandb.enable=true \
    --wandb.mode=offline \
    # ... 其他参数
```

训练完成后，在本地同步离线数据：

```bash
# 找到离线运行目录
find ./outputs -name "offline-run-*" -type d

# 同步到 Wandb
wandb sync <run_directory>/wandb/offline-run-*
```

## 配置说明

### 环境变量说明

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `WANDB_API_KEY` | Wandb API Key（必需） | 无 |
| `WANDB_PROJECT` | 项目名称 | `lerobot` |
| `WANDB_ENTITY` | 组织/用户名。需与 API Key 绑定的 entity 完全匹配；在组织下请用“用户名-组织”格式（例：`qiuyuhao19990704-sjtu`） | 空（默认使用登录用户名） |
| `WANDB_MODE` | 运行模式：`online`/`offline`/`disabled` | `online` |
| `WANDB_SILENT` | 静默模式，减少输出 | `True` |

### 训练命令参数说明

| 参数 | 说明 | 示例 |
|------|------|------|
| `--wandb.enable` | 启用 Wandb | `true` |
| `--wandb.project` | 项目名称 | `lerobot` |
| `--wandb.entity` | 组织/用户名（如组织下需用“用户名-组织”） | `qiuyuhao19990704-sjtu` |
| `--wandb.mode` | 运行模式 | `online`/`offline`/`disabled` |
| `--wandb.notes` | 运行备注 | `"实验描述"` |
| `--wandb.disable_artifact` | 禁用模型上传 | `true`/`false` |

## 完整训练示例

结合 `lerobot_env.md` 中的配置：

```bash
# 1. 激活 conda 环境
conda activate lerobot

# 2. 加载环境变量
export TOKENIZERS_PARALLELISM=False
export CUDA_VISIBLE_DEVICES=0
export MUJOCO_GL=egl
export PYTHONPATH=$PWD/src:$PYTHONPATH

# 3. 加载 Wandb 配置
source /home/kemove/qyh/lerobot/wandb_config.sh

# 4. 运行训练
lerobot-train \
    --policy.path=HuggingFaceVLA/smolvla_libero \
    --dataset.repo_id=HuggingFaceVLA/libero \
    --env.type=libero \
    --env.task=libero_10 \
    --output_dir=./outputs/ \
    --steps=100000 \
    --wandb.enable=true \
    --wandb.project=lerobot \
    --wandb.entity=qiuyuhao19990704-sjtu \
    --batch_size=256 \
    --num_workers=32 \
    --dataset.root=/home/kemove/.cache/huggingface/smolvla_datasets/libero
```

## 验证配置

检查 Wandb 配置是否正确：

```bash
# 检查环境变量
echo $WANDB_API_KEY
echo $WANDB_PROJECT
echo $WANDB_MODE

# 检查 Wandb 状态
wandb status
```

## 安全注意事项

1. **保护 API Key**：
   - 不要将 API Key 提交到 Git 仓库
   - 配置文件权限设置为仅自己可读：`chmod 600 /home/kemove/qyh/lerobot/wandb_config.sh`
   - 不要在其他用户可见的地方显示 API Key

2. **用户隔离**：
   - 此配置仅影响当前用户，不会影响其他用户
   - 环境变量只在当前 shell 会话中有效（除非添加到 `~/.bashrc` 或 `~/.zshrc`）

3. **文件权限**：
```bash
# 设置配置文件权限，仅自己可读写
chmod 600 /home/kemove/qyh/lerobot/wandb_config.sh
```

## 故障排除

### 问题1: "Not logged in" 错误

**解决方案**：
- 检查 `WANDB_API_KEY` 是否正确设置：`echo $WANDB_API_KEY`
- 确认已加载配置文件：`source /home/kemove/qyh/lerobot/wandb_config.sh`
- 验证 API Key 是否有效：访问 https://wandb.ai/settings 确认

### 问题2: 网络连接问题

**解决方案**：
- 使用离线模式：`export WANDB_MODE="offline"`
- 或在训练命令中指定：`--wandb.mode=offline`
- 训练完成后使用 `wandb sync` 同步数据

### 问题3: 权限错误（403 permission denied / upsertBucket）

**解决方案**：
- 检查配置文件权限：`ls -l /home/kemove/qyh/lerobot/wandb_config.sh`
- 设置正确权限：`chmod 600 /home/kemove/qyh/lerobot/wandb_config.sh`
- 确认 `WANDB_ENTITY` 与 API Key 绑定的用户名/组织完全一致；若在组织下需使用 “用户名-组织” 形式（如 `qiuyuhao19990704-sjtu`）

### 问题4: 项目不存在

**解决方案**：
- 在 Wandb 网站上创建项目：https://wandb.ai
- 或使用已存在的项目名称
- 确保 `WANDB_ENTITY` 设置正确（如果使用组织项目）

## 参考资源

- Wandb 官方文档：https://docs.wandb.ai
- Wandb Python SDK：https://docs.wandb.ai/ref/python
- API Key 管理：https://wandb.ai/settings

