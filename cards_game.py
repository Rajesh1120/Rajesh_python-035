import itertools
import random
#Andhar bahar game
def AndharBahargame(d):
    
    for i in range(1,10):
        print("**//**//**",end="")
    print()

    for i in range(1,10):
        print("**//**//**",end="")
    print()

    print("___________//*****//**WEL-COME TO ANDHAR AND BAHAR GAME**//*****//________________")
    print()
    
    print("""..........................How to play this Game .............................................""")
    print("""1.First, computer display one random card among all 52 cards.
            2.Secondly, the Computer ask you bid on Andhar(inside) or babhar(outside).
            3.if you feel the random card will be in Andhar list press a or A.
            4.if you feel the random card will be across in Baharr list press b or B.
            5.Next you want to bet on that card inital your score is 50 coins.
                i.Your bid was not exceed the total_score.
                ii.Your bid was not less than 4 coins.
            6.If your guessing correct you will won coins or else you lose your coins.""")
    print(""".....................................................................................""")
    print()
    print("If you want to start the game press 1 or if not press 0:")
    start=int(input())
    inital_user_score=50
    while (start):
        A=[0]
        B=[0]
        x=random.choice(d)
        card=x[1]
        if card == "diamond":
            card="♦"
        elif card == "heart":
            card="♥"
        elif card == "clubs":
            card="♣"
        else:
            card="♠"
            
        element=x[0][0]
        print("Card is provided by Computer is ==>  {" "} of {}".format(element,card))
        print()
        user_input=input("Enter Andhar ==> A or a and Bahaar ==>  B or b : ")
        print()
        if user_input not in ['a','b','A','B']:
            print("ERROR............please enter user_input should ['a','b','A','B'] in this list only")
            print()
        else:
            bid_amount=int(input("enter how many coins you want to bet INTIAL YOUR COINS ARE {}: ".format(inital_user_score)))
            print()
            if inital_user_score < 5 or inital_user_score < bid_amount or bid_amount < 0 or bid_amount < 5:
                print("Sorry! you don't have enough coins to play ")
                print()
                print("If you want to earn coins please play 2nd game called three cards ")
                print()
            else:
                flag=0
                while(1):
                    if element not in A:
                        y = random.choice(d)
                        A.append(y[0][0])
                    else:  
                        flag=65
                        break
                    if element not in B:
                        z = random.choice(d)
                        B.append(z[0][0])
                    else: 
                        flag=66
                        break
                   
                print("Andharr list ==>",A)
                print()
                print("Bahar list ==>",B)
                print()
                if flag == 65:
                    if user_input.upper() == "A":
                        print("Card is in Andharr")
                        print()
                        print("Congragulations ........! YOU WON ....  You chosse correct one ")
                        print()
                        inital_user_score+= (bid_amount)
                        print("YOUR SCORE = ",inital_user_score)
                    else:
                        print("Card is in Andharr")
                        print()
                        print("Sorry...........! YOU LOSE ........ You chosse wrong one ")
                        print()
                        inital_user_score-=bid_amount 
                        print("YOUR SCORE = ",inital_user_score)
                else:
                    
                    if user_input.upper() == "B":
                        print("Card is placed in Bahaar")
                        print()
                        print("Congragulations ........!YOU WON ........ You chosse correct one")
                        print()
                        inital_user_score+= (bid_amount)
                        print("YOUR SCORE = ",inital_user_score)
                    else:
                        print("Card is placed in Bahaar")
                        print()
                        print("Sorry...........! YOU LOSE........ You chosse wrong one")
                        print()
                        inital_user_score-=bid_amount 
                        print("YOUR SCORE = ",inital_user_score)
                print()
                print("___________________***** MATCH IS OVER *****__________________________")
                print()
                print()
            print("If you want to start the game again press 1 or if not press 0:")
            print()
            start=int(input())
            print()
    print(".............................THANK YOU FOR PLAYING................................")
    print()

#                                   threecardsgame
def Threecardsgame(d):
    
    print("___________//*****//**WELCOME TO THREE CARDS GAME**//*****//________________")
    print()
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
    
    computer=game(player_1,v)
    player2=game(player_2,v)
    
    
    if computer > player2:
        print("Congragulations............! The winner is computer")
        
    elif computer < player2 :
         print("Congragulations............! The winner is player2")
        
    else:
        print("Match is Draw")
    print()
    print("___________________***** MATCH IS OVER *****__________________________")

    print()

# main


if __name__=="__main__":
    print()
    print("\U0001F923____\U0001F923___\U0001F923____//*****//**WELCOME CARDS GAME**//*****//______\U0001F923_____\U0001F923_____\U0001F923")
    print()
    d=list(itertools.product(["1","2","3","4","5",'6','7','8','9','10',"J","Q","K","A"],["spade","heart","diamond","club"]))
    random.shuffle(d)
    print("/..................List of Games in Card games................/")
    print(" 1.AndharBahargame\n 2.Threecardsgame \n 3.exit() ")
    print("Please enter your choices")
    choiceofgametoplay=int(input())

    while(choiceofgametoplay):
        if choiceofgametoplay == 1:
            AndharBahargame(d)
        elif choiceofgametoplay==2:
            Threecardsgame(d)
        elif choiceofgametoplay == 3:
            print("___________//*****//**Thank you for playing**//*****//__________")
            exit()
        else:
            print("please check your choice:")
        print()
        print("/..................List of Games in Card games................/")
        print("1.AndharBahargame\n2.Threecardsgame\n3.exit() ")
        print("please enter your choices from list of games in cards")
        choiceofgametoplay=int(input())
        
        
        
        
        
