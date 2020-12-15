#Day4 Assignment1
#Write a program to open a file, writing 'I love Let's Upgrade', close it, read it again, close it, append some data to it and close it

filehand=open('MyFile.txt','w')
filehand.write('I love Let\'s Upgrade')
filehand.close()
filehand=open('MyFile.txt','r')
print(filehand.read())
filehand.close()
filehand.open('MyFile.txt','a')
filehand.write('We are learning Python')
filehand.close()
