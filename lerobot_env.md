# LeRobot 环境配置

## 环境安装

```bash
git clone https://github.com/huggingface/lerobot.git
cd lerobot

pip install -e ".[pi, smolvla, async, libero]"
pip install mujoco==3.3.2
pip install PyOpenGL_accelerate

pip install protobuf==6.33.0 grpcio==1.76.0
```

> **注意**：protobuf 和 grpcio 版本是必须的，因为改用了 grpc 协议，protobuf 使用新版本。原版本为 protobuf 6.31.0、grpcio 1.73.1。如果升级版本带来问题，请回退。

## 环境变量配置

```bash
export TOKENIZERS_PARALLELISM=False
export CUDA_VISIBLE_DEVICES=0
```

> **说明**：lerobot 里面的仿真和推理对 GPU 并行支持不好，上面两个环境变量需要设置使其单卡运行。训练时可以使用多卡。

```bash
export MUJOCO_GL=egl
export PYTHONPATH=$PWD/src:$PYTHONPATH
```

> **说明**：`MUJOCO_GL=egl` 用于不在屏幕上渲染，远程时没有屏幕需要使用这个。

## 使用已安装的环境

```bash
conda activate lerobot
```

## Wandb 配置（可选）

Wandb 用于训练过程的可视化监控和实验跟踪。

### 配置 Wandb

在使用 Wandb 前，需要先加载配置文件：

```bash
source /home/kemove/qyh/lerobot/wandb_config.sh
```

或者直接在命令中指定 Wandb 参数（详见下方命令示例）。

> **说明**：更多 Wandb 配置和使用方法，请参考 `wandb_usage.md` 文件。

## SmolVLA 训练和评估

### 训练流程概览（以示例命令为例）
- 初始化：解析配置、创建 Accelerator、设随机种子/设备；主进程先下载/加载数据集，创建评估环境，准备输出/日志目录并启动 wandb；构建策略、处理器、优化器与学习率调度。  
  - 标志性日志：`[INIT] ...` / `Creating dataset` / `Creating env` / `Creating policy`，以及 wandb run URL。
- 主训练循环：每步取 batch（batch_size=256，num_workers=32），前向→损失→反向→梯度裁剪→优化器/调度步进，记录日志与 wandb。  
  - 关注：`step`/`global_step`；loss、lr 的打印或 wandb 曲线。
- 定期评估：每 `eval_freq=1000` 步运行 `eval.n_episodes=1`，逐批 rollout 计算指标，写日志并同步 wandb。  
  - 标志性日志：`stepping through eval batches`、`running rollout with at most XXX steps`，评估指标输出（如 success/return）。
- 定期保存：每 `save_freq=1000` 步保存 checkpoint 到输出目录（`save_checkpoint=True`，不推 Hub 因为 `policy.push_to_hub=false`）。  
  - 标志性日志：`Saving checkpoint to ...` 或类似保存提示；检查 `outputs/.../checkpoints/step-*/`。
- 结束：达到总步数 `steps=100000` 后收尾，关闭 wandb、刷新日志/文件句柄。  
  - 标志性日志：`Training finished` / `end_training` / wandb run closed。

### 训练

#### 不使用 Wandb（默认）

```bash
lerobot-train \
    --policy.path=HuggingFaceVLA/smolvla_libero \
    --dataset.repo_id=HuggingFaceVLA/libero \
    --env.type=libero \
    --env.task=libero_10 \
    --output_dir=./outputs/ \
    --steps=100000 \
    --eval.batch_size=1 \
    --eval.n_episodes=1 \
    --eval_freq=1000 \
    --save_freq=1000 \
    --save_checkpoint=True \
    --policy.push_to_hub=false \
    --num_workers=32 \
    --batch_size=256 \
    --dataset.root=/home/kemove/.cache/huggingface/smolvla_datasets/libero
```

#### 使用 Wandb（推荐）

首先加载 Wandb 配置：

```bash
source /home/kemove/qyh/lerobot/wandb_config.sh
```

然后运行训练（Wandb 会自动使用环境变量中的配置）：

```bash
lerobot-train \
    --policy.path=HuggingFaceVLA/smolvla_libero \
    --dataset.repo_id=HuggingFaceVLA/libero \
    --env.type=libero \
    --env.task=libero_10 \
    --output_dir=./outputs/ \
    --steps=100000 \
    --eval.batch_size=1 \
    --eval.n_episodes=1 \
    --eval_freq=1000 \
    --save_freq=1000 \
    --save_checkpoint=True \
    --policy.push_to_hub=false \
    --num_workers=32 \
    --batch_size=256 \
    --dataset.root=/home/kemove/.cache/huggingface/smolvla_datasets/libero \
    --wandb.enable=true \
    --wandb.project=lerobot
```

> **注意**：如果遇到 `entity not found` 错误，请移除 `--wandb.entity` 参数，让 Wandb 使用默认 entity（你的用户名）。
> 或者确保 entity 名称正确（可以是你的用户名或组织名）。

**参数说明：**

| 参数 | 值 | 说明 |
|------|-----|------|
| `--policy.path` | `HuggingFaceVLA/smolvla_libero` | 使用 Hugging Face 上的 smolvla_libero 预训练策略 |
| `--dataset.repo_id` | `HuggingFaceVLA/libero` | 使用 libero 数据集 |
| `--env.type` | `libero` | 仿真环境类型为 libero |
| `--env.task` | `libero_10` | 具体的任务集为 libero_10 |
| `--output_dir` | `./outputs/` | 训练输出目录 |
| `--steps` | `100000` | 训练总步数 |
| `--eval.batch_size` | `1` | 评估时的 batch size |
| `--eval.n_episodes` | `1` | 评估时的 episode 数量 |
| `--eval_freq` | `1000` | 每 1000 步评估一次 |
| `--save_freq` | `1000` | 每 1000 步保存一次检查点 |
| `--save_checkpoint` | `True` | 启用保存检查点 |
| `--policy.push_to_hub` | `false` | 不自动上传模型到 Hub |
| `--num_workers` | `32` | 数据加载使用的进程数 |
| `--batch_size` | `256` | 训练的 batch size |
| `--dataset.root` | `/home/kemove/.cache/huggingface/smolvla_datasets/libero` | 数据集本地根目录 |
| `--wandb.enable` | `true` | 启用 Wandb 记录日志（仅在使用 Wandb 时需要） |
| `--wandb.project` | `lerobot` | Wandb 项目名称（可选，默认使用环境变量或 'lerobot'） |
| `--wandb.entity` | - | Wandb 组织/用户名（可选，不指定时使用默认用户名） |

### 评估

评估命令本身不支持直接使用 Wandb，但评估结果会自动保存到输出目录中，可以通过脚本手动上传到 Wandb。

#### 不使用 Wandb（默认）

```bash
lerobot-eval \
    --policy.path=HuggingFaceVLA/smolvla_libero \
    --env.type=libero \
    --env.task=libero_object \
    --eval.batch_size=1 \
    --eval.n_episodes=10 \
    --policy.n_action_steps=10 \
    --output_dir=./outputs/eval_results \
    --job_name=smolvla_eval
```

#### 使用 Wandb 可视化评估结果

评估脚本会将结果保存到 `--output_dir` 目录（包括视频和 `eval_info.json`），然后可以使用脚本上传到 Wandb：

```bash
# 1. 加载 Wandb 配置（可选，如果已在环境变量中配置）
source /home/kemove/qyh/lerobot/wandb_config.sh

# 2. 运行评估
lerobot-eval \
    --policy.path=HuggingFaceVLA/smolvla_libero \
    --env.type=libero \
    --env.task=libero_object \
    --eval.batch_size=1 \
    --eval.n_episodes=10 \
    --policy.n_action_steps=10 \
    --output_dir=./outputs/eval_results \
    --job_name=smolvla_eval

# 3. 上传评估结果到 Wandb
python /home/kemove/qyh/lerobot/upload_eval_to_wandb.py \
    --eval_dir ./outputs/eval_results \
    --project lerobot \
    --name smolvla_eval
```

> **说明**：`upload_eval_to_wandb.py` 脚本会自动上传评估指标（`eval_info.json`）和视频文件（`videos/*.mp4`）到 Wandb。
> 如果不指定 `--project` 和 `--name`，脚本会使用环境变量或默认值。

**参数说明：**

| 参数 | 值 | 说明 |
|------|-----|------|
| `--policy.path` | `HuggingFaceVLA/smolvla_libero` | 使用 Hugging Face 上的 smolvla_libero 策略进行评估 |
| `--env.type` | `libero` | 仿真环境类型 |
| `--env.task` | `libero_object` | 评估的具体任务集 |
| `--eval.batch_size` | `1` | 评估 batch size |
| `--eval.n_episodes` | `10` | 评估运行的 episode 数量 |
| `--policy.n_action_steps` | `10` | 策略每次推理输出的动作步数 |
| `--output_dir` | `./outputs/eval_results` | 评估结果保存目录 |
| `--job_name` | `smolvla_eval` | 评估任务名称 |

> **说明**：评估结果会保存在 `output_dir` 目录中，包括：
> - `eval_info.json`：评估指标（成功率、奖励等）
> - `videos/`：评估过程的视频文件

## PI0 训练

#### 不使用 Wandb

```bash
lerobot-train \
    --policy.path=/home/kemove/hyp/lerobot/pretrained_models/pi05_libero \
    --dataset.repo_id=HuggingFaceVLA/libero \
    --dataset.root=$HOME/.cache/huggingface/smolvla_datasets/libero \
    --batch_size=32 \
    --steps=6000 \
    --save_freq=2000 \
    --output_dir=outputs/pi05_libero_official_reproduce \
    --policy.push_to_hub=false \
    --policy.gradient_checkpointing=true \
    --resume=true
```

#### 使用 Wandb（推荐）

首先加载 Wandb 配置：

```bash
source /home/kemove/qyh/lerobot/wandb_config.sh
```

然后运行训练：

```bash
lerobot-train \
    --policy.path=/home/kemove/hyp/lerobot/pretrained_models/pi05_libero \
    --dataset.repo_id=HuggingFaceVLA/libero \
    --dataset.root=$HOME/.cache/huggingface/smolvla_datasets/libero \
    --batch_size=32 \
    --steps=6000 \
    --save_freq=2000 \
    --output_dir=outputs/pi05_libero_official_reproduce \
    --policy.push_to_hub=false \
    --wandb.enable=true \
    --wandb.project=lerobot \
    --policy.gradient_checkpointing=true \
    --resume=true
```

**参数说明：**

| 参数 | 值 | 说明 |
|------|-----|------|
| `--policy.path` | `/home/kemove/hyp/lerobot/pretrained_models/pi05_libero` | 预训练模型路径（本地绝对路径） |
| `--dataset.repo_id` | `HuggingFaceVLA/libero` | 数据集 ID |
| `--dataset.root` | `$HOME/.cache/huggingface/smolvla_datasets/libero` | 数据集本地缓存路径 |
| `--batch_size` | `32` | 训练 batch size |
| `--steps` | `6000` | 训练总步数 |
| `--save_freq` | `2000` | 每 2000 步保存一次 |
| `--output_dir` | `outputs/pi05_libero_official_reproduce` | 输出目录 |
| `--policy.push_to_hub` | `false` | 不上传到 Hub |
| `--wandb.enable` | `true` | 启用 Weights & Biases 记录日志（仅在使用 Wandb 时需要） |
| `--wandb.project` | `lerobot` | Wandb 项目名称（可选，默认使用环境变量或 'lerobot'） |
| `--wandb.entity` | - | Wandb 组织/用户名（可选，不指定时使用默认用户名） |
| `--policy.gradient_checkpointing` | `true` | 启用梯度检查点（节省显存） |
| `--resume` | `true` | 如果存在检查点，则恢复训练 |
