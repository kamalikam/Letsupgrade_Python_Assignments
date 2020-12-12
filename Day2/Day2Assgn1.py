#Assignment 1 Day 2
#Try five different functions of string
a='i am learning python'

capa=a.capitalize()                            #capitalize() for making the 1st character capital
print("Capitalization: ",capa)

capsa=a.upper()                               #upper() for changing the string to upper case
print('Upper case: ',capsa)

lowera=capsa.lower()                          #lower() for changing string to lower case
print('Lower case: ',lowera)

repla=a.replace('python','data science')      #replace() for replacing one word with another
print('Replaced Python with Data Science: ',repla)

parta=a.rpartition('learning')                #rpartition() to return tuple of string parted into 3 parts
print('Parted into three parts: ',parta)
