#!/usr/bin/env python3
"""
将 LeRobot 评估结果上传到 Wandb

用法:
    python upload_eval_to_wandb.py --eval_dir ./outputs/eval_results
    python upload_eval_to_wandb.py --eval_dir ./outputs/eval_results --project lerobot --name my_eval
    python upload_eval_to_wandb.py --eval_dir ./outputs/eval_results --project lerobot --entity my_entity

环境变量（可选）:
    WANDB_API_KEY: Wandb API Key
    WANDB_PROJECT: Wandb 项目名称（默认: lerobot）
    WANDB_ENTITY: Wandb 组织/用户名
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Optional

try:
    import wandb
except ImportError:
    print("错误: 未安装 wandb，请运行: pip install wandb")
    sys.exit(1)


def upload_eval_to_wandb(
    eval_dir: Path,
    project: Optional[str] = None,
    name: Optional[str] = None,
    entity: Optional[str] = None,
    job_type: str = "eval",
    notes: Optional[str] = None,
) -> None:
    """
    将评估结果上传到 Wandb

    Args:
        eval_dir: 评估结果目录（应包含 eval_info.json 和 videos/ 目录）
        project: Wandb 项目名称（默认从环境变量或 'lerobot'）
        name: Wandb run 名称（默认使用目录名）
        entity: Wandb 组织/用户名（默认从环境变量）
        job_type: Wandb job 类型（默认 'eval'）
        notes: Wandb run 备注
    """
    eval_dir = Path(eval_dir)
    
    if not eval_dir.exists():
        raise ValueError(f"评估目录不存在: {eval_dir}")
    
    # 获取配置（优先使用参数，其次环境变量，最后使用默认值）
    project = project or os.getenv("WANDB_PROJECT", "lerobot")
    entity = entity or os.getenv("WANDB_ENTITY", None)
    name = name or eval_dir.name
    
    print(f"准备上传评估结果到 Wandb...")
    print(f"  项目: {project}")
    print(f"  Run 名称: {name}")
    if entity:
        print(f"  Entity: {entity}")
    print(f"  评估目录: {eval_dir}")
    
    # 初始化 Wandb
    wandb.init(
        project=project,
        name=name,
        entity=entity,
        job_type=job_type,
        notes=notes,
    )
    
    try:
        # 上传评估指标
        eval_info_path = eval_dir / "eval_info.json"
        if eval_info_path.exists():
            print(f"\n读取评估指标: {eval_info_path}")
            with open(eval_info_path) as f:
                eval_info = json.load(f)
            
            # 上传整体指标
            if "overall" in eval_info:
                print("上传整体评估指标...")
                wandb.log(eval_info["overall"])
            
            # 上传每个任务的指标
            for task_group, task_info in eval_info.items():
                if task_group != "overall" and isinstance(task_info, dict):
                    # 将任务组名称作为前缀
                    for key, value in task_info.items():
                        if isinstance(value, (int, float)):
                            wandb.log({f"{task_group}/{key}": value})
            
            print("✓ 评估指标已上传")
        else:
            print(f"⚠ 警告: 未找到评估指标文件 {eval_info_path}")
        
        # 上传视频
        video_dir = eval_dir / "videos"
        if video_dir.exists() and video_dir.is_dir():
            video_files = list(video_dir.glob("*.mp4"))
            if video_files:
                print(f"\n找到 {len(video_files)} 个视频文件")
                for i, video_file in enumerate(video_files, 1):
                    print(f"  上传视频 {i}/{len(video_files)}: {video_file.name}")
                    wandb.log({f"eval_video_{i}": wandb.Video(str(video_file))})
                print("✓ 视频已上传")
            else:
                print(f"⚠ 警告: 视频目录 {video_dir} 中没有找到 .mp4 文件")
        else:
            print(f"⚠ 警告: 未找到视频目录 {video_dir}")
        
        print(f"\n✓ 评估结果已成功上传到 Wandb")
        print(f"  Run URL: {wandb.run.url}")
        
    except Exception as e:
        print(f"\n✗ 上传过程中出现错误: {e}")
        raise
    finally:
        wandb.finish()


def main():
    parser = argparse.ArgumentParser(
        description="将 LeRobot 评估结果上传到 Wandb",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "--eval_dir",
        type=str,
        required=True,
        help="评估结果目录路径（应包含 eval_info.json 和 videos/ 目录）"
    )
    
    parser.add_argument(
        "--project",
        type=str,
        default=None,
        help="Wandb 项目名称（默认: 从环境变量 WANDB_PROJECT 或 'lerobot'）"
    )
    
    parser.add_argument(
        "--name",
        type=str,
        default=None,
        help="Wandb run 名称（默认: 使用 eval_dir 的目录名）"
    )
    
    parser.add_argument(
        "--entity",
        type=str,
        default=None,
        help="Wandb 组织/用户名（默认: 从环境变量 WANDB_ENTITY）"
    )
    
    parser.add_argument(
        "--job_type",
        type=str,
        default="eval",
        help="Wandb job 类型（默认: 'eval'）"
    )
    
    parser.add_argument(
        "--notes",
        type=str,
        default=None,
        help="Wandb run 备注"
    )
    
    args = parser.parse_args()
    
    try:
        upload_eval_to_wandb(
            eval_dir=Path(args.eval_dir),
            project=args.project,
            name=args.name,
            entity=args.entity,
            job_type=args.job_type,
            notes=args.notes,
        )
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

