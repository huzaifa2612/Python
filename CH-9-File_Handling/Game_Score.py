import random

def game():
    print("You are playing Game")
    score=random.randint(1, 100)   # Score integer mai store howa
    with open("score.txt") as f:
        highscore=f.read()        #read krny sy highscore mai score string store kyu k hum score file mai string mai store kr rhy han
        if(highscore!=""):
          highscore=int(highscore)       #high score ko integer mai covert kiya
        else:  
          highscore=0

    print(f"Your Score is: {score}")
    if(score>highscore):                    # taa k comparison integer mai ho
        with open("score.txt", "w") as g:
            g.write(str(score))                   # score agar high ha to usko as tring store kiya 

    return score


game()