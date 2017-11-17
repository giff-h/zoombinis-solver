from lib.puzzle import AllergicCliffsNSE
from lib.zoombini import Zoombini


if __name__ == "__main__":
    party = Zoombini.party()
    puzzle = AllergicCliffsNSE()
    success = []
    choices = puzzle.choices

    for z in party:
        outcome = puzzle.attempt(z, choices[0])
        if not outcome:
            if puzzle.closed:
                break
            outcome = puzzle.attempt(z, choices[1])
        if outcome:
            success.append(z)

    print(puzzle._choices[0]._allergy, puzzle._choices[0]._inverted)
    print(party)
    print(success)
    print("Left {} behind".format(len(party) - len(success)))
