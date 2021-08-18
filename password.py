import random
string=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=[1,2,3,4,5,6,7,8,9,0]
schar=['!','@','#','$','%','^','&','*','~']
a=int(input("No. of characters you want in your password: "))
b=int(input("No. of number you want in your password: "))
c=int(input("No. of special characters you want in your password: "))
password=[]
for i in range(1,a+1):
    char=random.choice(string)
    password += char
for j in range(1,b+1):
    char=random.choice(num)
    password += str(char)
for i in range(1,c+1):
    char=random.choice(schar)
    password += char
random.shuffle(password)

pas=""
for char in password:
    pas += char
print(pas)