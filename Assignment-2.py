# ************* Answer -1 ****************
given_str="Python is a case sensitive language"

# length inbuilt function to find length (PART-A)
len_str=len(given_str)
print("Length of given string :",len_str)

# reverse string(PART-B)
rev_str=given_str[::-1]
print("Reverse of given string :",rev_str)

# slicing(PART-C)
sliced_str=given_str[10:26]
print("Slice of given string :",sliced_str)

# replacing (PART-D)
new_str=given_str.replace("a case sensitive","object oriented")
print("Slice of given string :",new_str)

# finding index(PART-E)
index=given_str.find("a")
print("Index of a in given string :",index)

# Removing spaces(PART-F)
new_str=given_str.replace(" ","")
print("After Removing spaces from given string :",new_str)


# # *********** Answer -2 ************
Name="Nitin"
SID=21105091
CGPA=9.9
department="ECE"
print("Hey",Name + " Here!\nMy SID is",SID,"\nI am from",department+" and my CGPA is",CGPA )


# *********** Answer -3 *************
a=56
b=10
# a
print("a&b :",a&b)
# b
print("a|b :",a|b)
# c
print("a^b :",a^b)
# d
print("a and b left shift with 2 bits = a :",a<<2,"and b :",b<<2)
# e
print("a right shift with 2 bits and b right shifts with 4 bits = a :",a>>2,"and b :",b>>4)


# *********** Answer -4 ***********
first_num=int(input("Enter the first number : "))
second_num=int(input("Enter the second number : "))
third_num=int(input("Enter the third number : "))
if(first_num>=second_num and first_num>=third_num):
    print("Largest number is",first_num)
elif(third_num>=second_num and first_num<=third_num):
    print("Largest number is",third_num)
elif(first_num<=second_num and second_num>=third_num):
    print("Largest number is",second_num)


# ************ Answer -5 ************
given_str=str(input("Enter string : "))
if(given_str.find('name')!=-1):
    print("Yes")
else:
    print("No")


# ************ Answer -6 ***********
Len_side1=int(input("Enter length of side 1st : "))
Len_side2=int(input("Enter length of side 2nd : "))
Len_side3=int(input("Enter length of side 3rd : "))
if(Len_side1>Len_side2+Len_side3 or Len_side2>Len_side3+Len_side1 or Len_side3>Len_side1+Len_side2):
    print("No")
else:
    print("Yes")
