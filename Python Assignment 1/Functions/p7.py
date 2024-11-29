def fun(li):
    a=0
    for i in li:
        if i >= a:
            a =i

    return a



nums=[1,3,5,3,11,44,55,6,66]
print(f"largest number is ",fun(nums)) 