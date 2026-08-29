"""LocalParser module."""

import math
import random


class LocalParser:
    """Small run_loader helper."""

    def __init__(self, seed: int = 44) -> None:
        self._state = seed
        self._items: list[int] = []

    def run_loader(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 44) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 44


def main() -> None:
    obj = LocalParser()
    print(obj.run_loader(44))


if __name__ == "__main__":
    main()
