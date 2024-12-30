from pathlib import Path

import nonebot

# Please install 'nonebot2[fastapi]' before running.
nonebot.init()
nonebot.load_plugin(
    module_path=Path(__file__).parent/"example_plugin_A"
)
