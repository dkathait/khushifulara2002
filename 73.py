#print 1 to 100 prime no.

min=1
max=100
for i in range(1,101):
    if i>1:
        for j in range(2,i): 
            if(i%j==0):
               break
        else:
            print(i)
    
