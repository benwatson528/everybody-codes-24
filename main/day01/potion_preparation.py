CREATURE_SCORES = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}


def solve(creature_groups) -> int:
    return sum(score_extra_potions(creature_group) +
               sum(CREATURE_SCORES[creature] for creature in creature_group)
               for creature_group in creature_groups)


def score_extra_potions(creature_group):
    match len([x for x in creature_group if x != "x"]):
        case 3:
            return 6
        case 2:
            return 2
        case _:
            return 0
