#check number is divisible by 5 and 11

a=int (input("enter any number = "))

if(a%5==0 and a%11==0):
    print("{0} is divisible by 5 and 11".format(a))
else:
    print("{0} is not divisible by 5 and 11".format(a))
