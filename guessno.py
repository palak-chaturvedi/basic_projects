#choose between hard and easy
import random
a=input("How do you want to play game??Easy or hard??").lower()
if a=="easy":
    n=10
else:
    n=5
#choose a number
a=random.randint(1,100)
print(a)
#iterate through no. of chances
i=0
while(i<n):
    i=i+1
    guess=int(input("guess the number:"))
    if a>guess:
        print("Number is too low!! Guess again")
    elif a<guess:
        print("Number is too high!! Guess again")
    else:
        print("correct guess")
        break
print("game ended!!")
