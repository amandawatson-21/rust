"""SimpleMonitor module."""

import math
import random


class SimpleMonitor:
    """Small render_collector helper."""

    def __init__(self, seed: int = 34) -> None:
        self._state = seed
        self._items: list[int] = []

    def render_collector(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 34) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 34


def main() -> None:
    obj = SimpleMonitor()
    print(obj.render_collector(34))


if __name__ == "__main__":
    main()
