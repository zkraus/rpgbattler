from .AbstractDie import AbstractDie
from random import randint


class Die6(AbstractDie):
    RESULT_FACES = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

    def __init__(self, weights=None):
        super().__init__(weights, sides=6)

    @property
    def result_face(self):
        return self.RESULT_FACES[self.result - 1]

    def __str__(self):
        return f"{self.result_face}"

    def roll(self):
        self._result = randint(1, 6)
        return self.result
