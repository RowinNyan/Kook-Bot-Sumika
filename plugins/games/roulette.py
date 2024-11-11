from .games import MultiGame
import random

class Roulette(MultiGame):
    _turn: int
    _hp: list[int]
    _bullets: list[bool]
    _items: list[list[int]]
    def __init__(self, num: int):
        super().__init__(num=num)
        self._id = 1
        self._turn = 0
        self._hp = []
        self._bullets = []
        self._items = []
    def isEnd(self) -> bool:
        if self._hp.count(0) == self._max_num-1: return True
        else: return False
    def next(self) -> None:
        while(True):
            self._turn = (self._turn + 1) % self._max_num
            if self._hp[self._turn] != 0: break
    def newGun(self) -> tuple[int, int]:
        real = random.randint(1, 5)
        fake = random.randint(1, 5)
        position = random.sample(range(real+fake), real)
        for i in range(real+fake):
            if i in position: self._bullets.append(True)
            else: self._bullets.append(False)
        return (real, fake)
    def shoot(self, target: int) -> bool:
        bullet = self._bullets.pop(0)
        if bullet:
            self._hp[target] -= 1
            self.next()
        else:
            if target != self._turn: self.next()
        return bullet
    def item(self):
        def a():
            ...
