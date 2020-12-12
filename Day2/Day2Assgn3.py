#Day2 Assignment 3
#Experiment with at least five different functions of dictionary
dict1={'Name':'Kam','Age':34,'Address':'Canada'}
print('\nDictionary1 is: ',dict1)

dict2=dict1.copy()                                     #copy() makes a copy of the dictionary
print('\nDictionary2 is a copy of Dictionary1: ',dict2)

dict=dict2.items()                                     #items() returns a tuple of key value pairs
print('\nTuple of key value pairs of Dictionary2 are: ',dict)

print('\nDictionary1 value for Address: ',dict1.setdefault('Address','Montreal'))     #setdefault gets value of specified key
print('Dictionary1 value for Phone Number: ',dict1.setdefault('Phone Number','9999999999'))
#If specified key is not there, the key with the specified value is inserted
print('Now new Dictionary1 is: ',dict1)

dict2.update({'Place of Birth':'India','State of Birth':'Jharkhand'})     #update() updates dictionary with given key value pairs
print('\nUpdated dictionary is: ',dict2)

x=dict2.values()                                         #values() returns a list of values
print('\nThe values are: ',x)
