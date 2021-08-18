auction={}
end_bid=False
while not end_bid:
    name=input("enter your name:")
    bid=int(input("input amount of bid:$"))
    auction[name]=bid
    a=input("do you wish to continue:")
    if a=="no":
        end_bid=True
high=0
for name in auction:
    if (auction[name]>high):
        high=auction[name]
        k=name
print(f"The highest bid is ${high} by {k}")
