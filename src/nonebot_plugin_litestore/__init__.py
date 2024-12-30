from nonebot.plugin import PluginMetadata

from .__main__ import *


__plugin_meta__ = PluginMetadata(
    name="轻量化的本地数据存储",
    description="开箱即用，更轻量地将插件数据存储至本地文件",
    usage=(
        '声明依赖: `require("nonebot_plugin_litestore")`\n'
        "导入所需文件夹:\n"
        "  `cache_dir = PluginStore.Cache.get_dir()`\n"
        '  `cache_file = PluginStore.Cache.get_file("file_name")`\n'
        "  `data_dir = PluginStore.Data.get_dir()`\n"
        '  `data_file = PluginStore.Data.get_file("file_name")`\n'
        "  `config_dir = PluginStore.Config.get_dir()`\n"
        '  `config_file = PluginStore.Config.get_file("file_name")`'
    ),
    type="library",
    homepage="https://github.com/kanbereina/nonebot-plugin-litestore",
    supported_adapters=None,
)


__all__ = ["PluginStore"]
