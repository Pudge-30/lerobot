#!/bin/bash
# Wandb 配置文件
# 使用方法: source /home/kemove/qyh/lerobot/wandb_config.sh
# 
# 注意：此配置文件仅影响当前 shell 会话，不会影响其他用户
# 如需持久化，请将以下环境变量添加到 ~/.bashrc 或 ~/.zshrc

# Wandb API Key（请替换为你的实际 API Key）
# 获取方式：访问 https://wandb.ai/settings 复制你的 API key
export WANDB_API_KEY="b463c028e0aece0278de23698f22401fbd3ecbfe"

# Wandb 项目配置（可选，也可以在训练命令中指定）
export WANDB_PROJECT="lerobot"
# WANDB_ENTITY 可选：如果不设置或留空，Wandb 会使用默认 entity（你的登录用户名）
# 如果遇到 "entity not found" 错误，请确保此行为空或注释掉
export WANDB_ENTITY="qiuyuhao19990704-sjtu"  # 仅在有需要时取消注释并填写

# Wandb 模式设置
# 可选值: online（在线模式，默认）, offline（离线模式）, disabled（禁用）
export WANDB_MODE="online"

# Wandb 静默模式（减少输出）
export WANDB_SILENT="True"

# 检查 API Key 是否已设置
if [ -z "$WANDB_API_KEY" ]; then
    echo "警告: WANDB_API_KEY 未设置，请编辑此文件并填入你的 API Key"
    echo "获取方式: https://wandb.ai/settings"
else
    echo "Wandb 配置已加载"
    echo "项目: ${WANDB_PROJECT:-默认项目}"
    echo "模式: ${WANDB_MODE}"
fi

