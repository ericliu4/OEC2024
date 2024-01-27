import random
def word_generate(difficulty, topMistake, secondMistake):

    file_path = "wordBank/wordBank.txt"
    word_list = []

    #open file
    with open(file_path, 'r') as file:
        for line in file:
            word_list.append(line.strip())
    

    if difficulty == 2: #generate word
        count = 1

    elif difficulty >= 3: #generate sentence
        count = 2
    #changed to max 2 words when difficulty >= 3

    curr = 0

    returnWord = ""

    while curr != count:
        word = random.choice(word_list)
        word = word.lower()

        #adjusted so that it would generate words/sentences the user is more likely to make a mistake on
        if word not in returnWord and len(word) <= difficulty+2 and (secondMistake == None or topMistake in word or secondMistake in word):
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

    topMistake = secondMistake = None
    topMistakeCounter = secondMistakeCounter = 0
    
    for key, value in game.mistakes.items():

        #update top and second top mistakes
        if value > topMistakeCounter:
            secondMistake = topMistake
            secondMistakeCounter = topMistakeCounter
            topMistake = key
            topMistakeCounter = value
        elif value > secondMistakeCounter:
            secondMistake = key
            secondMistakeCounter = value

    if difficulty == 1:
        return letter_generate()
    return word_generate(difficulty, topMistake, secondMistake)


#new change so that it would generate sentences the user is more likely to 
#make a mistake on



    


