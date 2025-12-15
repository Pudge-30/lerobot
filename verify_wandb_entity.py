# verify_wandb_entity.py
#!/usr/bin/env python3
import os
import sys

try:
    import wandb
    from wandb import Api
except ImportError:
    print("错误: 未安装 wandb")
    sys.exit(1)

api_key = os.getenv("WANDB_API_KEY")
if not api_key:
    print("错误: WANDB_API_KEY 未设置")
    sys.exit(1)

try:
    # 方法1: 使用 API Key 初始化
    api = Api(api_key=api_key)
    
    # 尝试获取当前用户信息
    try:
        # 在某些 wandb 版本中，viewer 是一个属性而不是方法
        viewer = api.viewer
        if callable(viewer):
            viewer_obj = viewer()
        else:
            viewer_obj = viewer
        actual_username = viewer_obj.username
    except (AttributeError, TypeError):
        # 方法2: 使用 wandb.init 然后获取用户名
        wandb.login(key=api_key, relogin=False)
        # 创建一个临时 run 来获取用户信息
        run = wandb.init(project="temp", mode="disabled")
        actual_username = run.entity
        wandb.finish()
        api = Api(api_key=api_key)
    
    configured_entity = os.getenv("WANDB_ENTITY", "未设置")
    
    print(f"API Key 对应的用户名: {actual_username}")
    print(f"配置的 WANDB_ENTITY: {configured_entity}")
    
    if configured_entity != "未设置" and configured_entity != actual_username:
        print(f"\n⚠ 警告: 配置的 entity ({configured_entity}) 与 API Key 对应的用户名 ({actual_username}) 不匹配！")
        print(f"建议: 使用以下命令修正（组织场景请用“用户名-组织”格式，例如 qiuyuhao19990704-sjtu）")
        print(f"export WANDB_ENTITY=\"{actual_username}\"")
    else:
        print("\n✓ Entity 配置正确")
        
except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)