"""AtomicFactory module."""

import math
import random


class AtomicFactory:
    """Small render_cache helper."""

    def __init__(self, seed: int = 55) -> None:
        self._state = seed
        self._items: list[int] = []

    def render_cache(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 55) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 55


def main() -> None:
    obj = AtomicFactory()
    print(obj.render_cache(55))


if __name__ == "__main__":
    main()
