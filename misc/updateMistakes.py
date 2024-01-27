from collections import Counter

def updateMistakes(game, generatedString, newString):
    generatedStringCounter = Counter(generatedString)
    newStringCounter = Counter(newString)
    
    for char, count in generatedStringCounter.items():

        # skip over space characters 
        if char == " ":
            continue


        #add to mistakes
        game.mistakes[char] += max(0, count - newStringCounter[char])


