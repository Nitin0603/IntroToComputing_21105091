# ******* Answer -1 *************

Given_str=str(input("Enter your string (Containing only alphabets(a-z or A-Z) and white spaces only) : "))
Two_word=False
# To check only one word is present or not
if ' ' in Given_str:
        Two_word=True
        Given_str+=' '
# To store word or its count 
Word_counter=dict()
word=''
for character in Given_str:
# if two word are present
    if(Two_word):
        if(character==' '):
            if(word in Word_counter):
                Word_counter[word]+=1
            elif(word!=''):
                Word_counter[word]=1
            word=''
        else:
            if(character!=' '):
                word+=character
# If only one word is present in given string
    else:
        if(character in Word_counter):
            Word_counter[character]+=1
        elif(character!=' '):
            Word_counter[character]=1
# printing of counting of word or char acc to que
for word in Word_counter:
    print("No of occurences of '%s' is %d"%(word,Word_counter[word]))


#  ************ Answer-2 *******************

# C1-MONTH C2-DAY C3-year

# input of month
C1=int(input("Enter month : "))
while(1>C1 or C1>12):
    print("Month can't be greater than 12 or less than 1")
    C1=int(input("Enter month again : "))
    if(1<=C1 and C1<=12):
        break
# input of year
C3=int(input("Enter year : "))
while(1800>C3 or C3>2025):
    print("Sorry,We can't solve for year greater than 2025 or less than 1800")
    C3=int(input("Enter year again : "))
    if(1800<=C3 and C3<=2025):
        break
#input of day
C2=int(input("Enter day : "))
if(C1==2 and C3%4==0):
    while(1>C2 or C2>29):
        print("For month-2 and leap year\nDay can't be greater than 29 or less than 1")
        C2=int(input("Enter day again : "))
        if(1<=C2 and C2<=29):
            break
elif(C1==2):
    while(1>C2 or C2>28):
        print("For month-2 and non-leap year\nDay can't be greater than 28 or less than 1")
        C2=int(input("Enter day again : "))
        if(1<=C2 and C2<=28):
            break
else: 
    if((C1%2==0 and C1>7)or(C1%2!=0 and C1<8)):
        while(1>C2 or C2>31):
            print("For Month-%d Day can't be greater than 31 or less than 1"%(C1))
            C2=int(input("Enter day again : "))
            if(1<=C2 and C2<=31):
                break
    else:
        while(1>C2 or C2>30):
            print("For Month-%d Day can't be greater than 30 or less than 1"%(C1))
            C2=int(input("Enter day again : "))
            if(1<=C2 and C2<=30):
                break 
if(C1==2):
    if(C2==29 or (C2==28 and C3%4!=0)):
        C2=1
        print("Next date while be in date/month/year is %d/%d/%d"%(C2,C1+1,C3))   
    else:
        print("Next date while be in date/month/year is %d/%d/%d"%(C2+1,C1,C3)) 
elif(C1==12 and C2==31):
    C1=1
    C2=1
    print("Next date while be in date/month/year is %d/%d/%d"%(C2,C1,C3+1))
elif(((C1%2==0 and C1>7) or (C1%2!=0 and C1<8)) and C2==31):
    C2=1
    print("Next date while be in date/month/year is %d/%d/%d"%(C2,C1+1,C3))
elif(((C1%2==0 and C1<8) or (C1%2!=0 and C1>7)) and C2==30):
    C2=1
    print("Next date while be in date/month/year is %d/%d/%d"%(C2,C1+1,C3))
else:
    print("Next date while be in date/month/year is %d/%d/%d"%(C2+1,C1,C3))


#  ************ Answer-3 *******************

lst=[3,9,12,15]
# list of ans which include tuples
lst_of_ans=[]
for lst_element in lst:
    tuple_ele_of_lst=(lst_element,lst_element*lst_element)
    lst_of_ans.append(tuple_ele_of_lst)
print(lst_of_ans)

#  ************ Answer-4 *******************

grade_point=int(input("Enter grade points : "))
if(grade_point==4):
    print("Your Grade is 'D' and Poor Perfomance")
elif(grade_point==5):
    print("Your Grade is 'C' and Below Average Perfomance")
elif(grade_point==6):
    print("Your Grade is 'C+' and Average Perfomance")
elif(grade_point==7):
    print("Your Grade is 'B' and Good Perfomance")
elif(grade_point==8):
    print("Your Grade is 'B+' and Very Good Perfomance")
elif(grade_point==9):
    print("Your Grade is 'A' and Excellent Perfomance")
elif(grade_point==10):
    print("Your Grade is 'A+' and Outstanding Perfomance")
else:
    print("Your Grade Points is out of range")

#  ************ Answer-5 *******************

Intial_str="ABCDEFGHIJK"
i=0
# For spaces setting in pattern
space=''
while(i<len(Intial_str)):
    print(space+Intial_str[0:len(Intial_str)-i])
    space+=' '
    i+=2

#  ************ Answer-6 *******************

Info_of_student=dict()
Add_more='Y'
Student_name=str(input("Enter name of student : "))
Student_SID=int(input("Enter SID of student : "))
Info_of_student[Student_name]=Student_SID
while(Add_more=='Y'):
    Add_more=str(input("You want to add more students\nIf yes write Y ,Else write N : "))
    if(Add_more=='N'):
        break
    elif(Add_more!='Y'):
        print("You Have to write only Y and N")
        Add_more='Y'
        continue
    Student_name=str(input("Enter name of student : "))
    if Student_name in Info_of_student:
        print("Student is already added")
        continue
    Student_SID=int(input("Enter SID of student : "))
    if Student_SID in Info_of_student.values():
        print("Student id is already alloted to student")
    else:
        Info_of_student[Student_name]=Student_SID

# Part-a
for student_name in Info_of_student:
    print("Student name is '%s' and SID is '%d'"%(student_name,Info_of_student[student_name]))

# Part-b
print(sorted(Info_of_student.items(),key = lambda t:t[0]))

# Part-c
print(sorted(Info_of_student.items(),key=lambda t:t[1]))

# Part-d
Student_SID_search=int(input("Enter Student SID to search : "))
find=False
for student in Info_of_student:
    if(Info_of_student[student]==Student_SID_search):
        find=True
        print("Student name is %s"%student)

if(find==False):
    print("Student id not exists")

#  ************ Answer-7 *******************

def fibonacci(no_of_ele):
    first_ele=0
    second_ele=1

    if(no_of_ele==1):
        print(first_ele)
        sum=0
    else:
        print(first_ele)
        print(second_ele)
        sum=1
        for i in range(2,no_of_ele):
            third_ele=first_ele+second_ele
            first_ele=second_ele
            second_ele=third_ele
            sum+=third_ele
            print(third_ele)
    print("Average of fibonacci is :",(sum/no_of_ele))
no_of_ele=int(input("Enter no. upto how much elements you want to print sequence and find avg : "))
fibonacci(no_of_ele)


#  ************ Answer-8 *******************

set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

# Part-a
ans_set_a=set1^set2
print(ans_set_a)

# Part-b
ans_set_b=set1^set2^set3
print(ans_set_b)

# Part-c
ans_set_c=(set1|set2|set3)-(set1&set2&set3)-ans_set_b
print(ans_set_c)

# Part-d
ans_set_d=set()
for i in range(1,10):
    if i not in set1:
        ans_set_d.add(i)      
print(ans_set_d)

# Part-e
ans_set_e=set()
for i in range(1,10):
    if i not in (set1|set2|set3):
        ans_set_e.add(i)
print(ans_set_e)