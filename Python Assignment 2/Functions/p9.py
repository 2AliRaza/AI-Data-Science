def pld(sen ):
    revers=sen[::-1]
    if revers== sen:
        return True
    else:
        return False
    


     

sentence=input("enter any string : ")
if pld(sentence):
    print("String is pledrom" )
else:
    print("String is not pledrom" )
    