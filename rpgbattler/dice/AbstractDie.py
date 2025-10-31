class AbstractDie:
    def __init__(self, weights=None, sides=6):
        self.sides = sides
        self.weights = weights
        if weights is None:
            self.weights = [1] * sides
        self._result = 1

    def __str__(self):
        return f"🎲{self.result}"

    def __repr__(self):
        return f"🎲{self.result}{self.weights}"

    def roll(self):
        raise NotImplementedError()

    def magic_roll(self, env):
        raise NotImplementedError()

    @property
    def result(self):
        return self._result

    def __int__(self):
        return self.result

    def __eq__(self, other):
        return self.result == int(other)

    def __lt__(self, other):
        return self.result < int(other)

    def __gt__(self, other):
        return self.result > int(other)

    def __add__(self, other):
        return self.result + int(other)

    def __sub__(self, other):
        return self.result - int(other)
