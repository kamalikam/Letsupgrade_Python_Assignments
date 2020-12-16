from cryptography.fernet import Fernet              #cryptography.fernet is the package and Fernet is the module
def generatekey():
    key=Fernet.generate_key()                       #A key is generated and returned
    return key


def getcontent():                                   # Function to get unencrypted input from user
    return input('Enter content to encrypt: ')


def encryptmessage(normalmessage,key):               #Function for encrypting the message
    k=Fernet(key)
    encryptedmessage=k.encrypt(normalmessage)
    return encryptedmessage


def decrypt(token,key):                              #Function for decrypting the encrypted message
    k=Fernet(key)
    decryptedmessage=k.decrypt(token)
    return decryptedmessage


x=getcontent().encode()                             #Converted string to bytes
key=generatekey()
em=encryptmessage(x,key)
print('Encrypted message is: ',em)
dm=decrypt(em,key)
print('Decrypted message is: ',dm)
