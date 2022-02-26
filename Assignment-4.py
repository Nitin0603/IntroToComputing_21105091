# ****** Que - 1 **********

def TowerOfHanoi(No_of_disc,Source,Destination,Helper):
    if(No_of_disc==0):
        return
    TowerOfHanoi(No_of_disc-1,Source,Helper,Destination)
    print(f'Move Disc {No_of_disc} from {Source} to {Destination}')
    TowerOfHanoi(No_of_disc-1,Helper,Destination,Source)


#  A,B,C are the polls & 3 disc 1<2<3   
#  We have to move all discs from Poll A to B By using C poll
TowerOfHanoi(3,'A','B','C')



# ****** Que - 2 **********

#  By recursive method 

def fac(n):
    if(n==1 or n==0):
        return 1
    return fac(n-1)*n

def combination(m,n):
    if(m==n or n==0):
        return 1
    return (int)((fac(m))/(fac(m-n)*fac(n)))

def printpascal(n,i):
    n-=1
    if(n<0):
        return
    if(n==0):
        print(' '*(i),end="")
        print(1,end="")
        return
    printpascal(n,i+1)
    print("")
    print(' '*(i),end="")
    m=n
    while(n>=0):
        print(combination(m,n),end=" ")
        n-=1

n=int(input("Enter the number rows of pascal's triangle : "))
printpascal(n,0)


# By iterative method 

print('\n')

def faci(n):
    if(n==0): return 1
    ans=1
    while(n>=1):
        ans*=n
        n-=1
    return ans

def icombination(m,n):
    if(m==n or n==0):
        return 1
    return (int)((faci(m))/(faci(m-n)*faci(n)))

n=int(input("Enter the number rows of pascal's triangle : "))
i=0
while(i<n):
    j=0
    print(' '*(n-i-1),end="")
    while(j<=i):
        print(icombination(i,j),end=" ")
        j+=1
    i+=1
    print('')



# ****** Que - 3 **********

n=int(input('Enter Number-1 : '))
m=int(input('Enter Number-2 : '))
result=divmod(n,m)

# part a
print(callable(result))

# part b
if 0 in result:
    print('False')
else:
    print('True')

# part c
new_result=(4,5,6)+result
list_to_print=[]
for ele in new_result:
    if (ele>4):
        list_to_print.append(ele)
print(list_to_print)

# part d
set_new_result=set(new_result)
print(set_new_result)

# part e
immutable_set=frozenset(set_new_result)
print(immutable_set)

# part f
max_ele=max(immutable_set)
print('Maximum element in set is %d and its hash value is %d'%(max_ele, hash(max_ele)))



# ****** Que - 4 **********

class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number=roll_number
    def __del__(self):
        print('Object destroyed')

Student_1=Student('xyz',1234567)
del Student_1
        

#  ******* Que - 5 ************

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary=salary
    def details(self):
        return f"   {self.name}   {self.salary}"

Employee_1=Employee('Mehak',40000)
Employee_2=Employee('Ashok',50000)
Employee_3=Employee('Viren',60000)
Employee_list=[Employee_1,Employee_2,Employee_3]
i=1
print('Employee   Name    Salary')
for employee in Employee_list:
    print(f'  {i}     {employee.details()}')
    i+=1



print( '\nPART - A :' )
Employee_list=[Employee_1,Employee_2,Employee_3]
Employee_list[0].salary=70000
i=1
print('Employee   Name    Salary')
for employee in Employee_list:
    print(f'  {i}     {employee.details()}')
    i+=1



print( '\nPART - B :' )
Employee_list=[Employee_1,Employee_2,Employee_3]
del Employee_3
Employee_list.pop(2)
i=1
print('Employee   Name    Salary')
for employee in Employee_list:
    print(f'  {i}     {employee.details()}')
    i+=1



# ****** Que - 6 **********

def permute(s):
    if s == "":
        return [s]
    else:
        ans = []
    for w in permute(s[1:]):
        for pos in range(len(w)+1):
            ans.append(w[:pos]+s[0]+w[pos:])
    return ans

word_by_George=str(input("Enter word : "))
word_speaked_by_barbie=str(input("Enter a new meaningfull word : "))
if word_speaked_by_barbie in permute(word_by_George):
    print("Friendship is real")
else:
    print("Friendship is fake")
