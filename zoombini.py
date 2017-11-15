from collections import namedtuple
from random import randrange


class Zoombini(namedtuple("Zoombini", ("feet", "nose", "eyes", "hair"))):
    __slots__ = ()

    @staticmethod
    def pick():
        return randrange(5)

    @classmethod
    def random(cls):
        return cls(cls.pick(), cls.pick(), cls.pick(), cls.pick())

    @classmethod
    def _some(cls, amount):
        return [cls.random() for _ in range(amount)]

    @classmethod
    def party(cls):
        party = sorted(cls._some(16))
        unique = sorted(set(party))
        redo = True
        while len(unique) <= 14 and redo:
            redo = False
            pos = 0
            for z in unique:
                # Count from pos onwards because any new preceeding zoombinis
                # could be identical, and would thus mess up the count
                count = party[pos:].count(z)
                if count > 2:
                    redo = True
                    start = pos + 2
                    end = pos + count
                    party[start:end] = cls._some(end - start)
                pos += count
            party = sorted(party)
            unique = sorted(set(party))
        return party


if __name__ == '__main__':
    from pprint import pprint

    pprint(Zoombini.party())
