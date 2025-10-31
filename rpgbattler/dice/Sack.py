class Sack:
    def __init__(self, dice=None):
        self.dice = dice
        if dice is None:
            self.dice = []

        self._histogram6 = []

    def add_die(self, die):
        self.dice.append(die)

    def roll(self):
        result = [x.roll() for x in self.dice]
        self.compute_histogram6()
        return result

    def __str__(self):
        return f"{''.join([str(x) for x in self.dice])}"

    def compute_histogram6(self):
        self._histogram6 = [self.dice.count(x) for x in range(1, 7)]

    @property
    def histogram6(self):
        return self._histogram6
