import inspect
from pathlib import Path
from typing import Optional

from nonebot.plugin import Plugin, get_plugin_by_module_name


def _get_caller_plugin() -> Optional[Plugin]:
    current_frame = inspect.currentframe()
    if current_frame is None:
        return None

    # find plugin
    frame = current_frame
    while frame := frame.f_back:
        module_name = (module := inspect.getmodule(frame)) and module.__name__
        if module_name is None:
            return None

        # skip nonebot_plugin_litestore it self
        if module_name.split(".", maxsplit=1)[0] == "nonebot_plugin_litestore":
            continue

        plugin = get_plugin_by_module_name(module_name)
        if plugin and plugin.id_ != "nonebot_plugin_litestore":
            return plugin

    return None


def try_get_caller_plugin() -> Plugin:
    if plugin := _get_caller_plugin():
        return plugin
    raise RuntimeError("Cannot detect caller plugin")


def get_plugin_path(
    base_dir: Path, plugin: Plugin
) -> Path:
    parts: list[str] = []
    plugin_id = plugin.id_
    while True:
        if ":" not in plugin_id:
            break

        plugin_id, part = plugin_id.rsplit(":", maxsplit=1)
        parts.append(part)

    return base_dir.joinpath(plugin_id, *reversed(parts))


__all__ = ["try_get_caller_plugin", "get_plugin_path"]
