CREATURE_SCORES = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}
EXTRA_PORTIONS = {3: 6, 2: 2, 1: 0, 0: 0}


def solve(creature_groups) -> int:
    return sum(EXTRA_PORTIONS[len([x for x in creature_group if x != "x"])] +
               sum(CREATURE_SCORES[creature] for creature in creature_group)
               for creature_group in creature_groups)
