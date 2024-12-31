import random
def game():
    print("You are playing the game....")
    score = random.randint(1, 50)
    with open('game.txt') as gm:
        high_score= gm.read()
        if (high_score != ""):
            high_score = int(high_score)
        else:
            high_score = 0
    print(f"Your score is: {score}")
    if (score > high_score):
        with open('game.txt', 'w') as gm:
            gm.write(str(score))
    return score

game()