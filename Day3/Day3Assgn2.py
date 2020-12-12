#Day3 Assignment 2
#Use for loop to print prime no.s between 1 and 100

prime=list()                        #Declared prime as a constructor of list type
for i in range(1,100):
    fact=0                          #Initialized number of factors as 0
    for j in range(1,i+1):
        if i%j==0:                  #If number is divisible. increase number of factors
            fact=fact+1
    if fact==2:                     #Prime number is divisible by 1 and itself only, so it has 2 factors only
        prime.append(i)
print(prime)
