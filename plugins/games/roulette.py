from typing import Callable

from .games import MultiGame
from ..random import random, randlist


class Roulette(MultiGame):

    _turn: int
    _next: int
    _hp: list[int]
    _bullets: list[bool]
    _items: list[list[int]]

    def __init__(self, num: int):
        super().__init__(num=num)
        self._id = 1
        self._turn = 0
        self._next = 1
        self._hp = []
        self._bullets = []
        self._items = []

    def isEnd(self) -> bool:
        if self._hp.count(0) == self._max_num-1: return True
        else: return False

    def next(self) -> None:
        while(True):
            self._turn = (self._turn + self._next) % self._max_num
            if self._hp[self._turn] != 0: break

    def newGun(self) -> tuple[int, int]:
        real = random.randint(1, 5)
        fake = random.randint(1, 5)
        position = random.sample(range(real+fake), real)
        for i in range(real+fake):
            if i in position: self._bullets.append(True)
            else: self._bullets.append(False)
        return (real, fake)
    
    def newItem(self) -> list[list[int]]:
        output = []
        for i in range(self._max_num):
            if self._hp[i] == 0: output.append([])
            else:
                sums = sum(self._items[i])
                news = 4 if sums <= 4 else 8 - sums
                newi = randlist(news, 8)
                nums = []
                for j in range(8): nums.append(newi.count(j))
                output.append(nums)
        return 
    
    def shoot(self, target: int) -> bool:
        bullet = self._bullets.pop(0)
        if bullet:
            self._hp[target] -= 1
            self.next()
        else:
            if target != self._turn: self.next()
        return bullet
    
    def item(self, item: str, *args, **kwargs):
        def glass() -> bool:
            return self._bullets[0]
        def phone() -> bool:
            if len(self._bullets) <= 2:
                raise Exception
            else:
                return self._bullets[random.randint(3, len(self._bullets)-1)]
        def smoke(id: int):
            self._hp[id] = self._hp[id] + 1 if self._hp[id] < 4 else 4
        def remote():
            self._next = -self._next
        def lock():
            ...
        def beer():
            return self._bullets.pop(0)
        def thief():
            ...
        def change() -> None:
            self._bullets[0] = not self._bullets[0]
        def knife():
            ...
        items: dict[str, Callable] = dict([i for i in locals().items() if isinstance(i[1], Callable)])
        item_id: dict[int, str] = {i: items[i] for i in range(8)}
        result = items[item](*args, **kwargs)
        return result
