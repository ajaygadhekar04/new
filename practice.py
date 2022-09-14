def fact(a):
    if a==1:
        return a
    else:
        return a * fact(a-1)
print(fact(7))

n=7
count=1
sum=1
while count<n:
    sum=sum*n
    n=n-1
print(sum)