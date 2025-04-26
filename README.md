<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebit-plugin-litestore

_✨ 轻量化 NoneBot 本地数据存储插件 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/kanbereina/nonebot-plugin-litestore.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-litestore">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-litestore.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">

</div>

> [!CAUTION]\
> **警告，本插件不是NoneBot2规范，商店插件请统一使用 LocalStore**

> [!IMPORTANT]
> 感谢项目 [**NoneBot Plugin LocalStore**](https://github.com/nonebot/plugin-localstore)
> 
> 本项目**在其基础上**对插件进行更改。

## 📖 介绍

为了**更加方便**管理插件数据，**开箱即用**，

本插件提供了与 [**NoneBot Plugin LocalStore**](https://github.com/nonebot/plugin-localstore) 不同的功能：


- [x] **无需配置，开箱即用**
- [x] **自动创建**插件数据存储路径
- [x] 创建**更加清晰**的插件数据路径


## 🔧 使用方式

加载插件后使用 `require` 声明插件依赖，直接使用本插件提供的<b>`PluginStore`</b>的**包装类**即可。

```python
from pathlib import Path
from nonebot import require

require("nonebot_plugin_litestore")

from nonebot_plugin_litestore import PluginStore as Store

plugin_cache_dir: Path = Store.cache.get_dir()
plugin_cache_file: Path = Store.cache.get_file("filename")
plugin_config_dir: Path = Store.config.get_dir()
plugin_config_file: Path = Store.config.get_file("filename")
plugin_data_dir: Path = Store.data.get_dir()
plugin_data_file: Path = Store.data.get_file("filename")
```

## 💡 存储路径

对于一个[**规范的NoneBot2项目**](https://nonebot.dev/docs/next/quick-start)，在**NoneBot完成初始化后**，调用本插件相关函数时，会自动在<b>`.env文件`所处目录</b>中创建路径。

比如：

**项目目录：Awesome**（包含<b>`.env文件`</b>）

则对应的路径为：**`./Awesome/__plugin_data__`**

---

假设你有一个叫 **`setu`** 的插件调用了 **`Store.data.get_dir()`**，<br>
则对应创建路径为： **`./Awesome/__plugin_data__/setu/data`**

---

同理，当你分别调用本插件的**不同函数**时，会**分别创建**以下路径：

① **`./Awesome/__plugin_data__/setu/data`**<br>
② **`./Awesome/__plugin_data__/setu/cache`**<br>
③ **`./Awesome/__plugin_data__/setu/config`**<br>

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
