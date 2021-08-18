import random
end_game=False
a=input("Press'y' if you want to play game and n to exit:")
if a =='n':
    end_game=True
elif a=='y':
    
    print('''
     _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/    ''')

cards=[2,3,4,5,6,7,8,9,10,11,10,10,10]
def calc(lst):
    total=0
    for i in lst:
        total+=i
        return total

ur_card=[]
comp_card=[]
while not end_game:
    card1=random.choice(cards)
    card2=random.choice(cards)
    card3=random.choice(cards)
    card4=random.choice(cards)
    ur_card.append(card1)
    ur_card.append(card2)
    comp_card.append(card3)
    print(ur_card)
    print(comp_card)
    b=input("press n to pass and y to take new card:")
    while(b=='y'):
        card5=random.choice(cards)
        ur_card.append(card5)
        calc(ur_card)
        p=card3+card4
        if 11 in ur_card and total>21:
            retu
        elif(total<21 and total>p):
            print("you lose")
        elif(total<21 and total<p):
            print("You win")
    if(b=='n'):
        sum=calc(ur_card)
    
        end_game=True


    
    