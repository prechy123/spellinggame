from tabulate import tabulate  # type: ignore
import csv
import random
import pyttsx3  # type: ignore


def main():
    username = input("Whats your username: ").capitalize().strip()
    level: int = get_user_level()
    difficulty: str = get_user_difficulty(level)
    words: list = get_words(difficulty)
    selected_words: set = select_five_words(words)
    score: int = user_spelling_score(selected_words)
    if score > 5:
        emoji = "( ͡👁️ ‿ ͡👁️ )"
    else:
        emoji = "¯\_( ͡° _> ͡°)_/¯"
    print(f"{username} final score is {score} {emoji}")
    save_score(username, score)
    get_current()


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


def get_words(difficulty) -> list:
    """
    Get words based on user difficulty selected
    :param difficulty: str of user difficulty
    :type difficulty: str
    :return: A list of string with words gotten from csv file
    :rtype: list
    """
    words = []
    with open("gamewords.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Difficulty"] == difficulty:
                words.append(row["Word"])
    return words


def select_five_words(words) -> set:
    """
    Gets eight unique random from list of words
    :param words: list of words gotting from difficulty
    :type words: list
    :return: A list of 8 unique words
    :rtype: list
    """
    selected_words = set()
    for _ in range(1000):
        selected_words.add(random.choice(words))
        if len(selected_words) == 8:
            break
    return selected_words


def user_spelling_score(selected_words) -> int:
    """
    Pronouce each word with robot voice and ask user to spell each word recording their score
    :param selected_words: A list of eight unique words
    :type selected_words: list
    :return: The user final score
    :rtype: int
    """
    score = 0
    life = 3
    for word in selected_words:
        headers = ["score", "life"]
        table = [
            [score, life],
        ]
        print("Your current score and life is ")
        print(tabulate(table, headers, tablefmt="simple_grid"))
        if life == 0:
            return score
        if score == 2 or score == 5:
            life += 1
        print("Pronouncing word...")
        word_to_audio(word)
        answer = input("Enter Spelling: ").capitalize()
        if answer == word:
            score += 1
            print("👍")
        else:
            life -= 1
            print("👎")
    return score


def word_to_audio(word):
    """
    Turns word to audio
    :param word: A word to be pronounces with pyttsx3
    :type word: str
    """
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.say(word)
    engine.runAndWait()


def save_score(username, score):
    """
    Saves the username and score in score.csv file
    :param username: The name of the current user
    :type username: str
    :param score: The final score of the current user
    :type score: int
    """
    with open("score.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "score"])
        # writer.writeheader()
        writer.writerow({"name": username, "score": score})


def get_current():
    current = input(
        "Enter {H} to get high-score \nEnter {C} to close game \nEnter {N} to start new game?\n"
    ).lower()
    match current:
        case "h":
            get_highscore()
            get_current()
        case "c":
            pass
        case "n":
            main()
        case _:
            print("Enter either {H, C or N}")


def get_highscore():
    print("highscore")


if __name__ == "__main__":
    main()
