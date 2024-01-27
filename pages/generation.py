import random

def run_generation(game):

    #file path
    file_path = "wordBank/wordBank.txt"
    word_list = []


    with open(file_path, 'r') as file:
        for line in file:
            word_list.append(line.strip())
    print(word_list)

    difficulty = game.get_difficulty()


    if difficulty == 1:
        count = 2

    elif difficulty == 2: #ignore this for now
        count = 3

    elif difficulty == 3: #ignore this for now
        count = 4
    curr = 0

    returnWord = ""

    while curr != count:
        word = random.choice(word_list)
        word = word.lower()
        if word not in returnWord:
            returnWord += " " + word
            curr += 1

    return returnWord


    


