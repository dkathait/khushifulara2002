#sum of digits in a no.

num=int(input("enter any number"))
sum=0
while(num>0):
    digit=num%10
    sum=sum+digit
    num=num//10
print("sum",sum)
