def count(a):
        count=0
        for i in range(len(a)):
            if a[i]=="a"or a[i]=="e" or a[i]=="i"  or a[i]=="o"  or a[i]=="u":
                  count += 1
        return count
 

string=input("Enter Any String : ")
print("number of vowels = ",count(string.lower()))

