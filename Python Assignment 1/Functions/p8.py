def fabc(num):
    a=0
    b=1
    if num==1:
        return a
    elif num==2:
        return b

    else:
        for i in range(2,num):
            a,b=b,a+b
    return b

    

num=int(input("enter which Fibonacci number to find : "))
print(f"{num}th Fibonacci Numbaer is ",fabc(num))
