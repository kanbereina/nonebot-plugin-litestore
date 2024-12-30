from abc import ABC, abstractmethod
from pathlib import Path


class Store(ABC):
    @staticmethod
    @abstractmethod
    def get_dir() -> Path:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def get_file(filename: str) -> Path:
        raise NotImplementedError


__all__ = ["Store"]
