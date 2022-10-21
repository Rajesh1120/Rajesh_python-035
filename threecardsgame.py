

import random
def game(gamer,v):
    max=0
    key=[]
    value=[]
    key=list(v.keys())
    value=list(v.values())
    for i in gamer:
        if i in key:
            c=key.index(i)
            max=max+value[c]
        else:
            print("sorry !, something went wrong:...")
    return max
    
if __name__=="__main__":
    print()
    print("___________//*****//**THREE CARDS GAME**//*****//________________")
    print()

    print("Description : Both players contains three cards in there list ,whose cards sum is maximum the player will will the game")

    print()
    v={'A':14, '2':2 ,'3':3, '4':4,'5':5,'6':6 ,
        '7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
    cards=['A','2','3','4','5','6','7','8','9','10','K','J','Q']
    player_1=[]
    player_2=[]
    for i in range(3):
        player_1.append(random.choice(cards))
        player_2.append(random.choice(cards))
    
    print("player1 three cards are ===>{} ".format(player_1))
    print()
    print("player2 three cards are ===> {}".format(player_2))
    print()
    
    player1=game(player_1,v)
    player2=game(player_2,v)
    
    
    if player1 > player2:
        print("Congragulations............! The winner is player1")

    elif player1 < player2 :
        print("Congragulations............! The winner is player2")
        
    else:
        print("Match is Draw")
    print()
    print("___________________***** MATCH IS OVER *****__________________________")
