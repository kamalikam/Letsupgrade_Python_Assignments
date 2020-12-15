#Day4 Assignment 2
#Write a function for returning the factorial of any number
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
x=input('Enter any number: ')
print('The factorial of ',x,' is ',fact(int(x)))
