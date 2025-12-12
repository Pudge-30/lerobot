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

## SmolVLA 训练和评估

### 训练

```bash
lerobot-train \
    --policy.path=HuggingFaceVLA/smolvla_libero \ # 使用 Hugging Face 上的 smolvla_libero 预训练策略
    --dataset.repo_id=HuggingFaceVLA/libero \ # 使用 libero 数据集
    --env.type=libero \ # 仿真环境类型为 libero
    --env.task=libero_10 \ # 具体的任务集为 libero_10
    --output_dir=./outputs/ \ # 训练输出目录
    --steps=100000 \ # 训练总步数
    --eval.batch_size=1 \ # 评估时的 batch size
    --eval.n_episodes=1 \ # 评估时的 episode 数量
    --eval_freq=1000 \ # 每 1000 步评估一次
    --save_freq=1000 \ # 每 1000 步保存一次检查点
    --save_checkpoint=True \ # 启用保存检查点
    --policy.push_to_hub=false \ # 不自动上传模型到 Hub
    --num_workers=32 \ # 数据加载使用的进程数
    --batch_size=256 \ # 训练的 batch size
    --dataset.root=/home/kemove/.cache/huggingface/smolvla_datasets/libero # 数据集本地根目录
```

### 评估

```bash
lerobot-eval \
    --policy.path=HuggingFaceVLA/smolvla_libero \ # 使用 Hugging Face 上的 smolvla_libero 策略进行评估
    --env.type=libero \ # 仿真环境类型
    --env.task=libero_object \ # 评估的具体任务集
    --eval.batch_size=1 \ # 评估 batch size
    --eval.n_episodes=10 \ # 评估运行的 episode 数量
    --policy.n_action_steps=10 # 策略每次推理输出的动作步数
```

## PI0 训练

```bash
lerobot-train \
    --policy.path=/home/kemove/hyp/lerobot/pretrained_models/pi05_libero \ # 预训练模型路径（本地绝对路径）
    --dataset.repo_id=HuggingFaceVLA/libero \ # 数据集 ID
    --dataset.root=$HOME/.cache/huggingface/smolvla_datasets/libero \ # 数据集本地缓存路径
    --batch_size=32 \ # 训练 batch size
    --steps=6000 \ # 训练总步数
    --save_freq=2000 \ # 每 2000 步保存一次
    --output_dir=outputs/pi05_libero_official_reproduce \ # 输出目录
    --policy.push_to_hub=false \ # 不上传到 Hub
    --wandb.enable=true \ # 启用 Weights & Biases 记录日志
    --policy.gradient_checkpointing=true \ # 启用梯度检查点（节省显存）
    --resume=true # 如果存在检查点，则恢复训练
```
