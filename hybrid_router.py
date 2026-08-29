"""AtomicMonitor module."""

import math
import random


class AtomicMonitor:
    """Small compute_handler helper."""

    def __init__(self, seed: int = 57) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_handler(self, count: int) -> list[int]:
        result = []
        for i in range(count):
            result.append((self._state + i * 57) % 997)
        self._items = result
        return result

    def total(self) -> int:
        return sum(self._items) or 57


def main() -> None:
    obj = AtomicMonitor()
    print(obj.compute_handler(57))


if __name__ == "__main__":
    main()
