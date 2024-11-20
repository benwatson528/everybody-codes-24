CREATURE_SCORES = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}
EXTRA_PORTIONS = {3: 6, 2: 2, 1: 0, 0: 0}


def solve(creature_groups) -> int:
    return sum(EXTRA_PORTIONS[len([c for c in cg if c != "x"])] +
               sum(CREATURE_SCORES[c] for c in cg)
               for cg in creature_groups)
