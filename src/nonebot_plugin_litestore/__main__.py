from pathlib import Path

from nonebot.config import ENV_FILE_SENTINEL

from .decorator import auto_create_dir
from .model import Store
from .utils import try_get_caller_plugin, get_plugin_path


BASE_DIR = ENV_FILE_SENTINEL.parent.cwd()/"__plugin_data__"


class PluginCache(Store):
    @staticmethod
    @auto_create_dir
    def get_dir() -> Path:
        plugin_path = get_plugin_path(
            base_dir=BASE_DIR,
            plugin=try_get_caller_plugin()
        )
        return plugin_path / "cache"

    @staticmethod
    def get_file(filename: str) -> Path:
        return PluginCache.get_dir() / filename


class PluginConfig(Store):
    @staticmethod
    @auto_create_dir
    def get_dir() -> Path:
        plugin_path = get_plugin_path(
            base_dir=BASE_DIR,
            plugin=try_get_caller_plugin()
        )
        return plugin_path / "config"

    @staticmethod
    def get_file(filename: str) -> Path:
        return PluginConfig.get_dir() / filename


class PluginData(Store):
    @staticmethod
    @auto_create_dir
    def get_dir() -> Path:
        plugin_path = get_plugin_path(
            base_dir=BASE_DIR,
            plugin=try_get_caller_plugin()
        )
        return plugin_path / "data"

    @staticmethod
    def get_file(filename: str) -> Path:
        return PluginData.get_dir() / filename


class PluginStore:
    cache = PluginCache
    config = PluginConfig
    data = PluginData


__all__ = ["PluginStore"]
