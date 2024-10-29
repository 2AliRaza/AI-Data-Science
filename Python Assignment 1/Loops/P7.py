num1=int(input("Enter a number to claculate its factorial : "))
num=num1
fac=1
while(num>0):
    fac=fac*num
    num=num-1
print(f"factorail of {num1} = : {fac}")