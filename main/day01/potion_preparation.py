def solve(creatures) -> int:
    return sum(sum_potions(creature) for creature in creatures)


def sum_potions(creature):
    match creature:
        case "B":
            return 1
        case "C":
            return 3
    return 0
