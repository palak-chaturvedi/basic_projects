import random
a=int(input("'Hii welcome to the game. press 0 for rock, 1 for ppr , 2 for scissor:'"))
comp=random.randint(0,2)
print (comp)
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print(f"you chose{a}")
img=[rock,paper,scissor]
print(img[a])
print(f"computer chose {comp}" )
print(img[comp])

if comp==2 and a==0:
    print("you win")
    
elif(comp>a):
    print("you lose")
elif(comp==a):
    print("draw")
elif(comp==0 and a==2):
    print("you lose")
else:
    print("you lose")
