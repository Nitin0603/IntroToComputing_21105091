# # Average of three numbers (Ans-1)

# first_number=int(input("Enter first number : "))
# second_number=int(input("Enter second number : "))
# third_number=int(input("Enter third number : "))
# AvgOfThreenumbers=(first_number+second_number+third_number)/3
# print("Average of three numbers :",AvgOfThreenumbers)


# # Computing a person income tax (Ans-2)

# Gross_income=int(input("Enter your Gross income : "))
# NumberOfDependent=int(input("Enter no of your Dependent(s) : "))
# # Calculating taxable income 
# standard_ded=10000
# dependent_ded=3000
# taxable_income=Gross_income-standard_ded-(dependent_ded*NumberOfDependent)
# # Calculating tax
# tax_rate=20
# tax=taxable_income*(tax_rate/100)
# print("Your tax is :",tax)


# # Store Data types into list (Ans-3)

# List_of_student_data=[]
# Student_SID=int(input("Enter your SID : "))
# List_of_student_data.append(Student_SID)
# Name=str(input("Enter your name : "))
# List_of_student_data.append(Name)
# Gender=str(input("Enter gender as F-female,M-male,U-unknown : "))
# List_of_student_data.append(Gender)
# course_name=str(input("Enter your course name : "))
# List_of_student_data.append(course_name)
# CGPA=float(input("Enter your CGPA : "))
# List_of_student_data.append(CGPA)
# print("List of student data :",List_of_student_data)


# # Sort list of 5 student marks (Ans-4)

# List_of_student_marks=[]
# Student_1=int(input("Enter marks of Student-1 : "))
# List_of_student_marks.append(Student_1)
# Student_2=int(input("Enter marks of Student-2 : "))
# List_of_student_marks.append(Student_2)
# Student_3=int(input("Enter marks of Student-3 : "))
# List_of_student_marks.append(Student_3)
# Student_4=int(input("Enter marks of Student-4 : "))
# List_of_student_marks.append(Student_4)
# Student_5=int(input("Enter marks of Student-5 : "))
# List_of_student_marks.append(Student_5)
# List_of_student_marks.sort()
# print("List of students marks :",List_of_student_marks)


# # # List of Colours (Ans-5)


# # part a (Removing 4th element)
# List_of_colours=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print("List of colours before removing :",List_of_colours)
# List_of_colours.pop(3)
# print("your list after removing 4th element :",List_of_colours)


# # part b (Clearing 3 to 4 and replace by purple)
# List_of_colours=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# print("List of colours before replacing :",List_of_colours)
# List_of_colours[3:5]=['Purple']
# print("your list after replacing black and pink with purple :",List_of_colours)



