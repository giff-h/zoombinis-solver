from random import randrange as _rand

from . import constants as _c


class AllergicCliffsNSE:
    def __init__(self):
        self._rule = (_rand(_c.Z_FEATURES), _rand(_c.Z_CHOICES_PER_FEATURE))
        self._attempts = 6

    def attempt(self, zoombini, bridge):
        if not self._attempts:
            return False

        self._attempts -= 1
        if zoombini[self._rule[0]] == self._rule[1]:
            return bridge
        else:
            return not bridge


if __name__ == "__main__":
    pass
