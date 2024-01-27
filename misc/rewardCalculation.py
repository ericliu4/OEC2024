from classes.GameData import GameData 


def reward_calculation(game, deletion, insertion, substitution, transposition):
    difficulty = game.get_difficulty()
    currScore = GameData.get_score()
    newScore = 0
    if difficulty == 1:
        newScore = 5
    elif difficulty == 2:
        newScore = 15
    elif difficulty == 3:
        newScore = 50
    
    newScore -= deletion
    newScore -= insertion
    newScore -= substitution
    newScore -= transposition

    
    currScore += max(0, newScore)

    return [0, currScore] if newScore < 0 else [newScore, currScore]





