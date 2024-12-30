<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebit-plugin-litestore

_✨ 新一代的轻量化 NoneBot 本地数据存储插件 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/kanbereina/nonebit-plugin-litestore.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebit-plugin-litestore">
    <img src="https://img.shields.io/pypi/v/nonebit-plugin-litestore.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">

</div>

> [!IMPORTANT]
> 感谢 [**NoneBot Plugin LocalStore**](https://github.com/nonebot/plugin-localstore)（Worked by [**yanyongyu**](https://github.com/yanyongyu)）！
> 
> 本项目**在其原有代码的基础上**、基于个人的需求，对插件进行更改。

## 📖 介绍

这里是插件的详细介绍部分

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebit-plugin-litestore

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebit-plugin-litestore
</details>
<details>
<summary>pdm</summary>

    pdm add nonebit-plugin-litestore
</details>
<details>
<summary>poetry</summary>

    poetry add nonebit-plugin-litestore
</details>
<details>
<summary>conda</summary>

    conda install nonebit-plugin-litestore
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebit_plugin_litestore"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| 配置项1 | 是 | 无 | 配置说明 |
| 配置项2 | 否 | 无 | 配置说明 |

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 指令1 | 主人 | 否 | 私聊 | 指令说明 |
| 指令2 | 群员 | 是 | 群聊 | 指令说明 |
### 效果图
如果有效果图的话
