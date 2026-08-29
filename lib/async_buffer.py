"""SimpleClient module."""

import math
import random


class SimpleClient:
    """Small sync_dispatcher helper."""

    def __init__(self, seed: int = 19) -> None:
        self._state = seed
        self._items: list[int] = []

    def sync_dispatcher(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 19) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 19


def main() -> None:
    obj = SimpleClient()
    print(obj.sync_dispatcher(19))


if __name__ == "__main__":
    main()
