import random
def word_generate(difficulty):

    file_path = "wordBank/wordBank.txt"
    word_list = []

    #open file
    with open(file_path, 'r') as file:
        for line in file:
            word_list.append(line.strip())
    

    if difficulty == 2: #generate word
        count = 1

    elif difficulty >= 3: #generate sentence
        count = difficulty


    curr = 0

    returnWord = ""

    while curr != count:
        word = random.choice(word_list)
        word = word.lower()
        if word not in returnWord and len(word) <= difficulty+2:
            returnWord += " " + word
            curr += 1
    print(returnWord)
    
    return returnWord

def letter_generate():

    file_path = "wordBank/letters.txt"
    letter_list = []

    #open file
    with open(file_path, 'r') as file:
        for line in file:
            letter_list.append(line.strip())

    return random.choice(letter_list)


def run_generation(game):
    difficulty = game.difficulty
    if difficulty == 1:
        return letter_generate()
    return word_generate(difficulty)





    


