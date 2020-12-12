#Day3 Assignment 4
#Print X prime numbers using while, taking X from user

prime=list()
X=input('How many prime numbers do you want to see? ')
counter=1
while counter<=int(X):
    fact=0
    j=1
    while j<=counter:
        if counter%j==0:
            fact=fact+1
        j=j+1
    counter=counter+1
    if fact==2:
        prime.append(counter)
print(prime)
