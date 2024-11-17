class Game:
    _id: int
    def __init__(self):
        super().__init__()
        self._id = 0

    @property
    def id(self) -> int:
        return self._id


class SingleGame(Game):
    def __init__(self):
        super().__init__()


class MultiGame(Game):

    _max_num: int
    _cur_num: int
    _players: list[str]

    def __init__(self, num: int):
        super().__init__()
        self._max_num = num
        self._cur_num = 0
        self._players = []

    def join(self, user: str) -> None:
        if not self.isReady():
            self._cur_num += 1
            self._players.append(user)

    def leave(self, user: str) -> None:
        if user in self._players:
            self._cur_num -= 1
            self._players.remove(user)
            
    def isReady(self) -> bool:
        return self._cur_num == self._max_num
