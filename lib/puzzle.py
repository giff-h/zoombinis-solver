from random import randrange as _rand

from . import constants as _c


class _Cliff:
    def __init__(self, allergy, inverted):
        self._allergy = allergy
        self._inverted = inverted

    def _attempt(self, zoombini):
        """
        Returns True if the zoombini crossed successfully, False if it did not.

        :param zoombini: A Zoombini object
        :return: A boolean
        """
        if zoombini[self._allergy[0]] == self._allergy[1]:
            return self._inverted
        else:
            return not self._inverted


class AllergicCliffsNSE:
    def __init__(self):
        self._attempts = 6
        rule = (_rand(_c.Z_FEATURES), _rand(_c.Z_CHOICES_PER_FEATURE))
        order = bool(_rand(2))
        self._choices = (_Cliff(rule, order), _Cliff(rule, not order))

    @property
    def choices(self):
        """
        Returns the choices that can be passed into `attempt`

        :return: A tuple
        """
        return tuple(range(len(self._choices)))

    @property
    def closed(self):
        return self._attempts == 0

    def attempt(self, zoombini, choice):
        if not self._attempts:
            return False

        result = self._choices[choice]._attempt(zoombini)
        if not result:
            self._attempts -= 1
        return result


if __name__ == "__main__":
    pass
