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

为了**更加方便**管理插件数据，**开箱即用**，

本插件提供了与 [**NoneBot Plugin LocalStore**](https://github.com/nonebot/plugin-localstore) 不同的功能：


- [x] **无需配置，开箱即用**
- [x] 自动在**NoneBot2规范机器人项目内**创建插件数据主文件夹
- [x] **更加清晰**的插件数据路径创建


## 使用方式

加载插件后使用 `require` 声明插件依赖，直接使用 `nonebot_plugin_litestore` 插件提供的类即可。

```python
from pathlib import Path
from nonebot import require

require("nonebot_plugin_litestore")

from nonebot_plugin_localstore import PluginStore as Store

plugin_cache_dir: Path = Store.Cache.get_dir()
plugin_cache_file: Path = Store.Cache.get_file("filename")
plugin_config_dir: Path = Store.Config.get_dir()
plugin_config_file: Path = Store.Config.get_file("filename")
plugin_data_dir: Path = Store.Data.get_dir()
plugin_data_file: Path = Store.Data.get_file("filename")
```

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
