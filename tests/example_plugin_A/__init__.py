from nonebot import require
from nonebot.log import logger

require("nonebot_plugin_litestore")

from nonebot_plugin_litestore import PluginStore as Store


plugin_data_dir = Store.data.get_dir()
plugin_config_dir = Store.config.get_dir()
plugin_cache_dir = Store.cache.get_dir()


logger.success(f"获取插件数据路径: {plugin_data_dir}")
logger.success(f"获取插件设定路径: {plugin_config_dir}")
logger.success(f"获取插件缓存路径: {plugin_cache_dir}")
