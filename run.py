from lib.puzzle import AllergicCliffsNSE
from lib.zoombini import Zoombini


if __name__ == "__main__":
    party = Zoombini.party()
    puzzle = AllergicCliffsNSE()
    success = []

    for z in party:
        outcome = puzzle.attempt(z, True)
        if not outcome:
            outcome = puzzle.attempt(z, False)
        if outcome:
            success.append(z)

    print("Left {} behind".format(len(party) - len(success)))
