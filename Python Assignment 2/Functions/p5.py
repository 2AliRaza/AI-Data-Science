def prime(a):
        prime=True
        for i in range(2,a):
            if a % i ==0:
                prime= False
        return prime            



num=int(input("Enter a Number to check Prime : "))
if prime(num):
    print("Numbers is Prime ")
else:
         print("Numbers is Not Prime ")


