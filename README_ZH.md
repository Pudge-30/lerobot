<p align="center">
  <img alt="LeRobot, Hugging Face Robotics Library" src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/lerobot-logo-thumbnail.png" width="100%">
  <br/>
  <br/>
</p>

<div align="center">

[![Tests](https://github.com/huggingface/lerobot/actions/workflows/nightly.yml/badge.svg?branch=main)](https://github.com/huggingface/lerobot/actions/workflows/nightly.yml?query=branch%3Amain)
[![Python versions](https://img.shields.io/pypi/pyversions/lerobot)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/huggingface/lerobot/blob/main/LICENSE)
[![Status](https://img.shields.io/pypi/status/lerobot)](https://pypi.org/project/lerobot/)
[![Version](https://img.shields.io/pypi/v/lerobot)](https://pypi.org/project/lerobot/)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.1-ff69b4.svg)](https://github.com/huggingface/lerobot/blob/main/CODE_OF_CONDUCT.md)
[![Discord](https://dcbadge.vercel.app/api/server/C5P34WJ68S?style=flat)](https://discord.gg/s3KuuzsPFb)

<!-- [![Coverage](https://codecov.io/gh/huggingface/lerobot/branch/main/graph/badge.svg?token=TODO)](https://codecov.io/gh/huggingface/lerobot) -->

</div>

<h2 align="center">
    <p><a href="https://huggingface.co/docs/lerobot/hope_jr">
        构建你自己的 HopeJR 机器人！</a></p>
</h2>

<div align="center">
  <img
    src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/hope_jr/hopejr.png"
    alt="HopeJR robot"
    title="HopeJR robot"
    width="60%"
  />

  <p><strong>认识一下 HopeJR – 一个用于灵巧操作的人形机器人手臂和手！</strong></p>
  <p>使用外骨骼和手套控制它，实现精确的手部动作。</p>
  <p>完美适用于高级操作任务！ 🤖</p>

  <p><a href="https://huggingface.co/docs/lerobot/hope_jr">
      在此查看完整的 HopeJR 教程。</a></p>
</div>

<br/>

<h2 align="center">
    <p><a href="https://huggingface.co/docs/lerobot/so101">
        构建你自己的 SO-101 机器人！</a></p>
</h2>

<div align="center">
  <table>
    <tr>
      <td align="center"><img src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/so101/so101.webp" alt="SO-101 follower arm" title="SO-101 follower arm" width="90%"/></td>
      <td align="center"><img src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/so101/so101-leader.webp" alt="SO-101 leader arm" title="SO-101 leader arm" width="90%"/></td>
    </tr>
  </table>

  <p><strong>认识一下升级版的 SO100，即 SO-101 – 每只手臂仅需 114 欧元！</strong></p>
  <p>只需在笔记本电脑上做几个简单的动作，几分钟内即可完成训练。</p>
  <p>然后坐下来看着你的作品自主行动！ 🤯</p>

  <p><a href="https://huggingface.co/docs/lerobot/so101">
      在此查看完整的 SO-101 教程。</a></p>

  <p>想更进一步？通过构建 LeKiwi 让你的 SO-101 动起来！</p>
  <p>查看 <a href="https://huggingface.co/docs/lerobot/lekiwi">LeKiwi 教程</a>，让你的机器人装上轮子充满活力。</p>

  <img src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/lekiwi/kiwi.webp" alt="LeKiwi mobile robot" title="LeKiwi mobile robot" width="50%">
</div>

<br/>

<h3 align="center">
    <p>LeRobot: 面向真实世界机器人的最先进 AI</p>
</h3>

---

🤗 LeRobot 旨在为 PyTorch 中的真实世界机器人提供模型、数据集和工具。我们的目标是降低机器人的入门门槛，让每个人都能从共享数据集和预训练模型中受益并做出贡献。

🤗 LeRobot 包含专注于模仿学习（Imitation Learning）和强化学习（Reinforcement Learning）的最先进方法，这些方法已被证明可以迁移到真实世界中。

🤗 LeRobot 已经提供了一套预训练模型、包含人类采集演示的数据集以及仿真环境，让你无需组装机器人即可开始使用。在接下来的几周内，我们计划增加对目前最实惠和功能最强大的真实世界机器人的支持。

🤗 LeRobot 在此 Hugging Face 社区页面上托管预训练模型和数据集：[huggingface.co/lerobot](https://huggingface.co/lerobot)

#### 仿真环境上的预训练模型示例

<table>
  <tr>
    <td><img src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/gym/aloha_act.gif" width="100%" alt="ACT policy on ALOHA env"/></td>
    <td><img src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/gym/simxarm_tdmpc.gif" width="100%" alt="TDMPC policy on SimXArm env"/></td>
    <td><img src="https://raw.githubusercontent.com/huggingface/lerobot/main/media/gym/pusht_diffusion.gif" width="100%" alt="Diffusion policy on PushT env"/></td>
  </tr>
  <tr>
    <td align="center">ALOHA 环境上的 ACT 策略</td>
    <td align="center">SimXArm 环境上的 TDMPC 策略</td>
    <td align="center">PushT 环境上的 Diffusion 策略</td>
  </tr>
</table>

## 安装

LeRobot 适用于 Python 3.10+ 和 PyTorch 2.2+。

### 环境设置

创建一个包含 Python 3.10 的虚拟环境并激活它，例如使用 [`miniforge`](https://conda-forge.org/download/)：

```bash
conda create -y -n lerobot python=3.10
conda activate lerobot
```

使用 `conda` 时，在你的环境中安装 `ffmpeg`：

```bash
conda install ffmpeg -c conda-forge
```

> **注意：** 这通常会为你的平台安装使用 `libsvtav1` 编码器编译的 `ffmpeg 7.X`。如果不支持 `libsvtav1`（使用 `ffmpeg -encoders` 检查支持的编码器），你可以：
>
> - _[在任何平台上]_ 显式安装 `ffmpeg 7.X`：
>
> ```bash
> conda install ffmpeg=7.1.1 -c conda-forge
> ```
>
> - _[仅限 Linux]_ 安装 [ffmpeg 构建依赖](https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu#GettheDependencies) 并 [从源码编译带有 libsvtav1 的 ffmpeg](https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu#libsvtav1)，并确保你通过 `which ffmpeg` 使用的是对应的 ffmpeg 二进制文件。

### 安装 LeRobot 🤗

#### 从源码安装

首先，克隆仓库并进入目录：

```bash
git clone https://github.com/huggingface/lerobot.git
cd lerobot
```

然后，以可编辑模式安装库。如果你计划为代码做贡献，这很有用。

```bash
pip install -e .
```

> **注意：** 如果遇到构建错误，你可能需要安装额外的依赖项（`cmake`、`build-essential` 和 `ffmpeg libs`）。在 Linux 上，运行：
> `sudo apt-get install cmake build-essential python3-dev pkg-config libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libswscale-dev libswresample-dev libavfilter-dev`。对于其他系统，请参阅：[编译 PyAV](https://pyav.org/docs/develop/overview/installation.html#bring-your-own-ffmpeg)

对于仿真，🤗 LeRobot 附带了 gymnasium 环境，可以作为 extras 安装：

- [aloha](https://github.com/huggingface/gym-aloha)
- [xarm](https://github.com/huggingface/gym-xarm)
- [pusht](https://github.com/huggingface/gym-pusht)

例如，要安装带有 aloha 和 pusht 的 🤗 LeRobot，请使用：

```bash
pip install -e ".[aloha, pusht]"
```

### 从 PyPI 安装

**核心库：**
安装基础包：

```bash
pip install lerobot
```

_这仅安装默认依赖项。_

**额外功能：**
要安装附加功能，请使用以下命令之一：

```bash
pip install 'lerobot[all]'          # 所有可用功能
pip install 'lerobot[aloha,pusht]'  # 特定功能 (Aloha & Pusht)
pip install 'lerobot[feetech]'      # Feetech 电机支持
```

_将 `[...]` 替换为你需要的功能。_

**可用标签：**
有关可选依赖项的完整列表，请参阅：
https://pypi.org/project/lerobot/

> [!NOTE]
> 对于 lerobot 0.4.0，如果你想安装 pi 标签，你需要执行：`pip install "lerobot[pi]@git+https://github.com/huggingface/lerobot.git"`。
>
> 这将在下一个补丁版本中解决。

### Weights & Biases

要使用 [Weights and Biases](https://docs.wandb.ai/quickstart) 进行实验跟踪，请登录：

```bash
wandb login
```

(注意：你还需要在配置中启用 WandB。见下文。)

### 可视化数据集

查看 [示例 1](https://github.com/huggingface/lerobot/blob/main/examples/dataset/load_lerobot_dataset.py)，它演示了如何使用我们的数据集类，该类会自动从 Hugging Face Hub 下载数据。

你也可以通过在命令行执行我们的脚本来本地可视化 Hub 上的数据集片段：

```bash
lerobot-dataset-viz \
    --repo-id lerobot/pusht \
    --episode-index 0
```

或者使用 `root` 选项和 `--mode local` 可视化本地文件夹中的数据集（在以下情况下，将在 `./my_local_data_dir/lerobot/pusht` 中搜索数据集）：

```bash
lerobot-dataset-viz \
    --repo-id lerobot/pusht \
    --root ./my_local_data_dir \
    --mode local \
    --episode-index 0
```

它将打开 `rerun.io` 并显示摄像头流、机器人状态和动作，如下所示：

https://github-production-user-asset-6210df.s3.amazonaws.com/4681518/328035972-fd46b787-b532-47e2-bb6f-fd536a55a7ed.mov?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240505%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240505T172924Z&X-Amz-Expires=300&X-Amz-Signature=d680b26c532eeaf80740f08af3320d22ad0b8a4e4da1bcc4f33142c15b509eda&X-Amz-SignedHeaders=host&actor_id=24889239&key_id=0&repo_id=748713144

我们的脚本还可以可视化存储在远程服务器上的数据集。查看 `lerobot-dataset-viz --help` 获取更多说明。

### `LeRobotDataset` 格式

`LeRobotDataset` 格式的数据集使用起来非常简单。它可以从 Hugging Face Hub 上的仓库加载，也可以从本地文件夹加载，例如 `dataset = LeRobotDataset("lerobot/aloha_static_coffee")`，并且可以像任何 Hugging Face 和 PyTorch 数据集一样进行索引。例如 `dataset[0]` 将从数据集中检索单个时间帧，包含观察值（observation）和动作（action），作为 PyTorch 张量准备输入模型。

`LeRobotDataset` 的一个特点是，我们可以通过设置 `delta_timestamps` 为相对于索引帧的时间列表，基于与索引帧的时间关系来检索多个帧，而不是通过索引检索单个帧。例如，使用 `delta_timestamps = {"observation.image": [-1, -0.5, -0.2, 0]}`，对于给定的索引，可以检索 4 帧：索引帧之前的 1 秒、0.5 秒和 0.2 秒的 3 个“前序”帧，以及索引帧本身（对应于 0 条目）。有关 `delta_timestamps` 的更多详细信息，请参阅示例 [1_load_lerobot_dataset.py](https://github.com/huggingface/lerobot/blob/main/examples/dataset/load_lerobot_dataset.py)。

在底层，`LeRobotDataset` 格式利用多种方式序列化数据，如果你计划更深入地使用此格式，了解这些会很有用。我们试图制作一种灵活而简单的数据集格式，它可以涵盖强化学习和机器人技术（仿真和真实世界）中存在的大多数类型的特征和特性，重点关注摄像头和机器人状态，但只要可以用张量表示，就可以轻松扩展到其他类型的感知输入。

以下是用 `dataset = LeRobotDataset("lerobot/aloha_static_coffee")` 实例化的典型 `LeRobotDataset` 的重要细节和内部结构组织。确切的特征会因数据集而异，但主要方面不会改变：

```
dataset attributes:
  ├ hf_dataset: 一个 Hugging Face 数据集 (基于 Arrow/parquet)。典型特征示例:
  │  ├ observation.images.cam_high (VideoFrame):
  │  │   VideoFrame = {'path': mp4 视频路径, 'timestamp' (float32): 视频中的时间戳}
  │  ├ observation.state (list of float32): 手臂关节位置 (例如)
  │  ... (更多观察值)
  │  ├ action (list of float32): 手臂关节目标位置 (例如)
  │  ├ episode_index (int64): 此样本的剧集索引
  │  ├ frame_index (int64): 此样本在剧集中的帧索引 ; 每个剧集从 0 开始
  │  ├ timestamp (float32): 剧集中的时间戳
  │  ├ next.done (bool): 指示剧集结束 ; 每个剧集的最后一帧为 True
  │  └ index (int64): 整个数据集中的通用索引
  ├ meta: 一个 LeRobotDatasetMetadata 对象，包含:
  │  ├ info: 数据集的元数据字典
  │  │  ├ codebase_version (str): 用于跟踪创建数据集的代码库版本
  │  │  ├ fps (int): 数据集录制/同步的每秒帧数
  │  │  ├ features (dict): 数据集中包含的所有特征及其形状和类型
  │  │  ├ total_episodes (int): 数据集中的总剧集数
  │  │  ├ total_frames (int): 数据集中的总帧数
  │  │  ├ robot_type (str): 用于录制的机器人类型
  │  │  ├ data_path (str): parquet 文件的格式化字符串
  │  │  └ video_path (str): 视频文件的格式化字符串 (如果使用视频)
  │  ├ episodes: 包含剧集元数据的 DataFrame，列包括:
  │  │  ├ episode_index (int): 剧集索引
  │  │  ├ tasks (list): 此剧集的任务列表
  │  │  ├ length (int): 此剧集中的帧数
  │  │  ├ dataset_from_index (int): 此剧集在数据集中的起始索引
  │  │  └ dataset_to_index (int): 此剧集在数据集中的结束索引
  │  ├ stats: 数据集中每个特征的统计信息 (max, mean, min, std) 字典，例如
  │  │  ├ observation.images.front_cam: {'max': tensor with same number of dimensions (e.g. `(c, 1, 1)` for images, `(c,)` for states), etc.}
  │  │  └ ...
  │  └ tasks: 包含任务信息的 DataFrame，任务名称作为索引，task_index 作为值
  ├ root (Path): 存储数据集的本地目录
  ├ image_transforms (Callable): 应用于视觉模态的可选图像变换
  └ delta_timestamps (dict): 用于时间查询的可选 delta 时间戳
```

`LeRobotDataset` 使用几种广泛使用的文件格式对其每个部分进行序列化，即：

- hf_dataset 使用 Hugging Face datasets 库序列化存储为 parquet
- 视频存储为 mp4 格式以节省空间
- 元数据存储为纯 json/jsonl 文件

可以从 HuggingFace Hub 无缝上传/下载数据集。要在本地数据集上工作，如果它不在默认的 `~/.cache/huggingface/lerobot` 位置，你可以使用 `root` 参数指定其位置。

#### 复现最先进 (SOTA) 结果

我们在 [Hub 页面](https://huggingface.co/lerobot) 上提供了一些可以实现最先进性能的预训练策略。
你可以通过加载其运行配置来复现它们的训练。只需运行：

```bash
lerobot-train --config_path=lerobot/diffusion_pusht
```

即可复现 PushT 任务上 Diffusion Policy 的 SOTA 结果。

## 贡献

如果你想为 🤗 LeRobot 做贡献，请查看我们的 [贡献指南](https://github.com/huggingface/lerobot/blob/main/CONTRIBUTING.md)。

### 添加预训练策略

一旦你训练了一个策略，你可以使用类似 `${hf_user}/${repo_name}` 的 hub id 将其上传到 Hugging Face Hub (例如 [lerobot/diffusion_pusht](https://huggingface.co/lerobot/diffusion_pusht))。

你首先需要找到位于实验目录内的 checkpoint 文件夹 (例如 `outputs/train/2024-05-05/20-21-12_aloha_act_default/checkpoints/002500`)。其中有一个 `pretrained_model` 目录，应该包含：

- `config.json`: 策略配置的序列化版本 (遵循策略的 dataclass config)。
- `model.safetensors`: 一组 `torch.nn.Module` 参数，以 [Hugging Face Safetensors](https://huggingface.co/docs/safetensors/index) 格式保存。
- `train_config.json`: 包含用于训练的所有参数的综合配置。策略配置应与 `config.json` 完全匹配。这对于任何想要评估你的策略或进行复现的人都很有用。

要将这些上传到 hub，请运行以下命令：

```bash
huggingface-cli upload ${hf_user}/${repo_name} path/to/pretrained_model
```

请参阅 [lerobot_eval.py](https://github.com/huggingface/lerobot/blob/main/src/lerobot/scripts/lerobot_eval.py) 以获取其他人如何使用你的策略的示例。

### 致谢

- LeRobot 团队 🤗 构建了 SmolVLA [论文](https://arxiv.org/abs/2506.01844), [博客](https://huggingface.co/blog/smolvla)。
- 感谢 Tony Zhao, Zipeng Fu 及其同事开源了 ACT 策略、ALOHA 环境和数据集。我们的版本改编自 [ALOHA](https://tonyzhaozh.github.io/aloha) 和 [Mobile ALOHA](https://mobile-aloha.github.io)。
- 感谢 Cheng Chi, Zhenjia Xu 及其同事开源了 Diffusion 策略、Pusht 环境和数据集，以及 UMI 数据集。我们的版本改编自 [Diffusion Policy](https://diffusion-policy.cs.columbia.edu) 和 [UMI Gripper](https://umi-gripper.github.io)。
- 感谢 Nicklas Hansen, Yunhai Feng 及其同事开源了 TDMPC 策略、Simxarm 环境和数据集。我们的版本改编自 [TDMPC](https://github.com/nicklashansen/tdmpc) 和 [FOWM](https://www.yunhaifeng.com/FOWM)。
- 感谢 Antonio Loquercio 和 Ashish Kumar 的早期支持。
- 感谢 [Seungjae (Jay) Lee](https://sjlee.cc/), [Mahi Shafiullah](https://mahis.life/) 及其同事开源了 [VQ-BeT](https://sjlee.cc/vq-bet/) 策略并帮助我们将其代码库改编到我们的仓库中。该策略改编自 [VQ-BeT repo](https://github.com/jayLEE0301/vq_bet_official)。

## 引用

如果你愿意，可以使用以下方式引用这项工作：

```bibtex
@misc{cadene2024lerobot,
    author = {Cadene, Remi and Alibert, Simon and Soare, Alexander and Gallouedec, Quentin and Zouitine, Adil and Palma, Steven and Kooijmans, Pepijn and Aractingi, Michel and Shukor, Mustafa and Aubakirova, Dana and Russi, Martino and Capuano, Francesco and Pascal, Caroline and Choghari, Jade and Moss, Jess and Wolf, Thomas},
    title = {LeRobot: State-of-the-art Machine Learning for Real-World Robotics in Pytorch},
    howpublished = "\url{https://github.com/huggingface/lerobot}",
    year = {2024}
}
```

## Star 历史

[![Star History Chart](https://api.star-history.com/svg?repos=huggingface/lerobot&type=Timeline)](https://star-history.com/#huggingface/lerobot&Timeline)

