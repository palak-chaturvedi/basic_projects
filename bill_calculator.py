a=float(input("Total bill:"))
b=int(input("No. of persons bill will be distributed in:"))
c=int(input("Amount of tip percent you want to give:"))
bill=(a+((c*a)/100))/b
print(f"Eac one has to pay:{bill}")