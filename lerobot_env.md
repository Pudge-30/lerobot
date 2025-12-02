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

### 评估

```bash
lerobot-eval \
    --policy.path=HuggingFaceVLA/smolvla_libero \
    --env.type=libero \
    --env.task=libero_object \
    --eval.batch_size=1 \
    --eval.n_episodes=10 \
    --policy.n_action_steps=10
```

## PI0 训练

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
    --policy.gradient_checkpointing=true \
    --resume=true
```
