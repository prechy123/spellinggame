from tabulate import tabulate


def main():
    level: int = get_user_level()
    difficulty: str = get_user_difficulty(level)
    
def get_user_level() -> int:
    """
    get user level and using tabulate package to format level table
    :return: An Int of level selected
    :rtype: Int
    """
    headers = ["Level", "Difficulty"]
    table = [
        [1, "Beginner"],
        [2, "Intermediate"],
        [3, "Advanced"],
        [4, "Expert"],
        [5, "Impossible"],
        ]
    print(tabulate(table, headers, tablefmt="simple_grid"))
    while True:
        level = input("Enter level[1-5]: ")
        match level:
            case "1" | "2" | "3" | "4" | "5":
                return int(level)
            case _:
                print("level must be in range of 1 to 5")
                continue
    
def get_user_difficulty(level) -> str:
    """
    Get user difficulty
    :param level: User selected level
    :type level: int
    :return: A string of selected difficulty based on level
    :rtype: str
    """
    match level:
        case 1:
            return "Beginner"
        case 2:
            return "Intermediate"
        case 3:
            return "Advanced"
        case 4:
            return "Expert"
        case 5:
            return "Impossible"
        case _:
            return "None"
if __name__ == "__main__":
    main()