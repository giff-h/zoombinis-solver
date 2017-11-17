from collections import namedtuple as _nt
from random import randrange as _rand

from . import constants as _c


class Zoombini(_nt("Zoombini", ("feet", "nose", "eyes", "hair"))):
    __slots__ = ()

    @staticmethod
    def pick():
        return _rand(_c.Z_CHOICES_PER_FEATURE)

    @classmethod
    def random(cls):
        return cls(cls.pick(), cls.pick(), cls.pick(), cls.pick())

    @classmethod
    def _some(cls, amount):
        return [cls.random() for _ in range(amount)]

    @classmethod
    def party(cls):
        party = sorted(cls._some(_c.Z_PARTY_SIZE))
        unique = sorted(set(party))
        redo = True
        while len(unique) <= (14) and redo:  # TODO refactor this number to be derived from constants
            redo = False
            pos = 0
            for z in unique:
                # Count from pos onwards because any new preceeding zoombinis
                # could be identical, and would thus mess up the count
                count = party[pos:].count(z)
                if count > _c.Z_COMMON_IN_PARTY:
                    redo = True
                    start = pos + _c.Z_COMMON_IN_PARTY
                    end = pos + count
                    party[start:end] = cls._some(end - start)
                pos += count
            party = sorted(party)
            unique = sorted(set(party))
        return party


if __name__ == "__main__":
    from pprint import pprint

    pprint(Zoombini.party())
