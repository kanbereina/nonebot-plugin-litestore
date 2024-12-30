from nonebot import require
from nonebot.log import logger

require("nonebot_plugin_litestore")

from nonebot_plugin_litestore import PluginStore as Store  # noqa


plugin_data_dir = Store.Data.get_dir()
plugin_config_dir = Store.Config.get_dir()
plugin_cache_dir = Store.Cache.get_dir()


logger.success(f"获取插件数据路径: {plugin_data_dir}")
logger.success(f"获取插件设定路径: {plugin_config_dir}")
logger.success(f"获取插件缓存路径: {plugin_cache_dir}")
