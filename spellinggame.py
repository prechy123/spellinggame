from tabulate import tabulate #type: ignore
import csv
import random
import pyttsx3


def main():
    level: int = get_user_level()
    difficulty: str = get_user_difficulty(level)
    words = get_words(difficulty)
    selected_words = select_five_words(words)
    score = user_spelling_score(selected_words)
    if score > 5:
        emoji = "( ͡👁️ ‿ ͡👁️ )"
    else:
        emoji = "¯\_( ͡° _> ͡°)_/¯"
    print(f"Your final score is {score} {emoji}")
    
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
        
def get_words(difficulty):
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
   
def select_five_words(words):
    """
    Gets eight unique random from list of words
    :param words: list of words gotting from difficulty
    :type words: list
    :return: A list of 8 unique words
    :rtype: list
    """
    selected_words = set()
    for i in range(1000):
        selected_words.add(random.choice(words))
        if len(selected_words) == 8:
            return selected_words
   
def user_spelling_score(selected_words):
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
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    engine.say(word)
    engine.runAndWait()
    
        
if __name__ == "__main__":
    main()