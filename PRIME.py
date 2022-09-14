for n in range (1,50):
    count=0
    for i in range (2,n):
        if n%i==0:
            count=count+1
            break
    if count==0:
        print(n,end=' ')
#=================

n=12
count=0
i=0
while n>=count:
    if n%2==0:
        i=i+1
    #count=count+1
if i==0:
    print(n,'no is prime')
else:
    print(n,'no is not prime')

