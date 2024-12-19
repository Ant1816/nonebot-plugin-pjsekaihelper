<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-pjsekaihelper

_✨ 世界计划小助手 ✨_

![LICENSE](https://img.shields.io/github/license/Ant1816/nonebot-plugin-pjsekaihelper.svg)
[![PYPI](https://img.shields.io/pypi/v/nonebot-plugin-pjsekaihelper.svg)](https://pypi.python.org/pypi/nonebot-plugin-pjsekaihelper)
![Python3.9+](https://img.shields.io/badge/Python-3.9+-blue)
![nonebot2](https://img.shields.io/badge/NoneBot2-2.3.1+-red)
![onebotv11](https://img.shields.io/badge/OneBot-v11-yellow)

</div>

## 📖 介绍

世界计划插件，拥有组建车队等功能，持续开发中

<div align="center">

## 有问题或想法欢迎提issue以及pr！！！

</div>

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-pjsekaihelper

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-pjsekaihelper
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-pjsekaihelper
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-pjsekaihelper
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-pjsekaihelper
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_pjsekaihelper"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| 无 | 无 | 无 | 无 |

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| pjsk help | 群员 | 否 | 群聊 | 获取指令帮助 |
| 建车队/组队/组车队 <房间号> <服务器(日/台/韩/国际/中)> | 群员 | 否 | 群聊 | 创建一个车队 |
| 删除车队/删队/删车队 <房间号> | 群主/管理员/SUPERUSER | 否 | 群聊 | 删除指定车队 |
| 车队号/房间号/车号/有烤吗/有烤嘛/ycm | 群员 | 否 | 群聊 | 发送房间列表 |
| 重置车队列表 | SUPERUSER | 否 | 群聊 | 清空房间列表 |

## ⌨ 开发计划
&#x1F7E9; 跨群车队组建

&#x1F7E8; 表情包生成

&#x1F7E5; 随机抽卡

&#x1F7E5; 用户数据处理
 
## 效果图
![效果图](https://raw.githubusercontent.com/Ant1816/Ant1816/refs/heads/main/pjsekai.png)
