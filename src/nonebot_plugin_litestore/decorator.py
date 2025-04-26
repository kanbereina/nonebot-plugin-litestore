import functools
from pathlib import Path
from typing import Callable

from typing_extensions import ParamSpec


P = ParamSpec("P")


def _ensure_dir(path: Path) -> None:
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
    elif not path.is_dir():
        raise RuntimeError(f"{path} is not a directory")


def auto_create_dir(func: Callable[P, Path]) -> Callable[P, Path]:
    """一个装饰器, 用于自动创建路径"""
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Path:
        path = func(*args, **kwargs)
        _ensure_dir(path)
        return path

    return wrapper


__all__ = ["auto_create_dir"]
