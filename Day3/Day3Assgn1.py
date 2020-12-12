#Day3 Assignment 1
#Use if, else and elif to print your report card

sub=list()                                                      #Declared constructors of type list for subjects, marks and grades
marks=list()
grades=list()
num=input('Enter number of subjects: ')                         #Took number of subjects from user
for i in range(0,int(num)):
  sub.append(input('Enter name of subject one by one: '))       #Took names of subjects one by one from user and populated list 'sub'
for j in range(0,int(num)):
    print('Enter marks of ',sub[j],': ',end=' ')                #Toom subject wise marks from user and populated list 'marks'
    marks.append(input())
for k in range(0,int(num)):

#95-100 A+, 90-94 A, 85-89 B+, 80-84 B, 75-79 C+, 70-74 C, 60-69 D, 50-59 E, <50 self.fail

    if float(marks[k])>=95:
        grades.append('A+')
    elif float(marks[k])>=90 and float(marks[k])<=94:
        grades.append('A')
    elif float(marks[k])>=85 and float(marks[k])<=89:
        grades.append('B+')
    elif float(marks[k])>=80 and float(marks[k])<=84:
        grades.append('B')
    elif float(marks[k])>=75 and float(marks[k])<=79:
        grades.append('C+')
    elif float(marks[k])>=70 and float(marks[k])<=74:
        grades.append('C')
    elif float(marks[k])>=60 and float(marks[k])<=69:
        grades.append('D')
    elif float(marks[k])>=50 and float(marks[k])<=59:
        grades.append('E')
    else:
        grades.append('Fail')
print('\nSubject        ','Marks        ','Grades')
print('___________________________________________\n')

for l in range(0,int(num)):
    print(sub[l],'              ',marks[l],'                ',grades[l])
