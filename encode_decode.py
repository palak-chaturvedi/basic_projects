alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode():

    word=input("enter word:")
    n=int(input("want to shift character by:"))
    text=""
    for ch in word:
        pos=alphabet.index(ch)
        new_pos=pos+n
        text += alphabet[new_pos]
    print(text)
def decode():
    word=input("enter word:")
    n=int(input("want to shift character by:"))
    text=""
    for ch in word:
        pos=alphabet.index(ch)
        new_pos=pos-n
        text += alphabet[new_pos]
    print(text)

a=input("you want to encode or decode:").lower()
if (a=="encode"):
    encode()
elif(a=="decode"):
    decode()
else:
    print("bhai shi daal le yrr")