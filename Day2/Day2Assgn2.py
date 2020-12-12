#Day2 Assignment 2
#Five different functions of lists
numlist1=[12,34,1,-6,8.4,-9.6,0,4]
numlist2=numlist1                   #Made a duplicate of numlist1
strlist1=['Harry','Sunaina','Orange','Laptop']
strlist2=strlist1                   #Made a duplicate of strlist1

numlist1.extend(strlist1)           #extend() to extend 1st string by 2nd string
print('\nList1 extended by list2 is: ',numlist1)

ind=numlist1.index(-6)               #index() for returning index of -6
print('\nThe index of -6 in numlist1 is: ',ind)

numlist1.pop(3)                     #pop() for removing 4th item of the list
print('\nAfter popping 4th item of numlist1: ',numlist1)

numlist3=numlist2.clear()           #clear() for deleting all elements of a list
print('\nnumlist2 is cleared: ',numlist3)


strlist2.insert(0,'Ghana')           #insert() adds a specified value to a specified position of a list
print('\nAdded Ghana to 1st position of strlist2: ',strlist2)
