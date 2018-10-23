#ASSIGNMENT- DECISION AND FLOW CONTROL
#Q.1- Take an input year from user and decide whether it is a leap year or not
# -----------------one way------------------------------------------------------------------------------------------------------------
'''year=int(input("Year:"))
if(year%4==0):
    print("leap year")
else:
    print("Not a leap year")
'''
#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
'''
print("Specify the dimension of quadrilateral:")
length = int(input("Length:"))
breadth = int(input("Breadth:"))
if(length==breadth):
    print("quadrillateral is square.")
else:
    print("quadrillateral is rectangle.")
'''
#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
'''print("Enter age of 3 person:")
age1=int(input("person 1:"))
age2=int(input("person 2:"))
age3=int(input("person 3:"))
if(age1>age2):
    if(age1>age3):
        print("person1 oldest")
    else:
        print("person3 oldest")
else:
    if(age2>age3):
        print("person2 oldest")
    else:
        print("person3 oldest")
'''        
#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

#1. if employee is female, then she will work only in urban areas. 
#2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
#3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
#4. And any other input of age should print "ERROR".
'''
print("Hello! enter the following Details:")
age = int(input("Age:"))
sex = input("Sex as M or F:")
ms = input("marital status as Y or N :")
if(sex=='F'):
    print("she will work in urban areas.")
elif(sex=='M'):
    if(20<age & age<40):
        print("he can work anywhere.")
    elif(40<age & age<60):
        print("he will work in urban areas only.")
    else:
        print("Error!")
else:
    print("Error!")'''
#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
'''
Qty=int(input("Specify quantity of objects:"))
price = 100;
total_cost =Qty*price
if(total_cost>1000):
    discount = total_cost*(10/100)
    New_total_cost = total_cost-discount
    print("Total Cost:")
    print(New_total_cost)
else:
    print("Total Cost:")
    print(total_cost)
    '''
#Q.1- Take 10 integers from user and print it on screen.
'''
i = 10
for i in range (1,11):
    print(i)'''
#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
"""
while 1:
    print(".")
"""
#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
'''
print("Input integer elements of list.")
H=[]
G=[]

for I in range (0,10,1):
    P=int(input("in:"))
    H.append(P)
    G.append(P*P)
print(H)
print(G)
'''
#Q.4- From a list containing ints, strings and floats, make three lists to store them separately
'''
a= [1,2,3,"foo","bar","baz",1.00,2.00,3.00]
Ints=[]
Strings=[]
Floats=[]
for k in range(0,9):
    m=type(a[k])
    print(m)
    if(m==int):
        Ints.append(a[k])
    if(m==str):
        Strings.append(a[k])
    if(m==float):
        Floats.append(a[k])
print(Ints)
print(Strings)
print(Floats)
'''
#Q.5- Using range(1,101), make a list containing only prime numbers.
'''
P=[]
for j in range(1,102):
    X=[]
    a=j
    for i in range(a-1,1,-1):
        c= a%i
        X.append(c)
    if all ([c!=0 for c in X]):
        P.append(a)
print(P)
print("The list of all prime number between 1 to 101")
'''
#Q.6- Print the following patterns: 
#       * 
#       ** 
#       *** 
#       ****
'''
for i in range(1,5):
    print("*"*i)
    '''
#Q.7- Take inputs from user to make a list. Again take one input from user and search it in
#     the list and delete that element, if found. Iterate over list using for loop. 
'''
V = []
o=10
for o in range(0,10):
    q=int(input("element : "))
    V.append(q)
print(V)
X=int(input("Enter Any Element which you want to find and remove"))
for o in range(0,10):
    if(V[o]==X):
        V.remove(X)
print(V)
'''
print("for convenience the comments are used each time I mentioned program so that we can remove comments one by one and execute programs -thanks")
