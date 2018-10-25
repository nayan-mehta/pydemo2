#Syntax of a class
# class Classname:
#     <statement 1>
#     .
#     .
#     .
#     < statement N >

#Class objects support two kinds of operations: Attribute reference and Class instantiation
#Attribute reference
# class MyClass:
#     '''A simple class example'''
#     i=12345
#
#     def f(self):
#         return "Hello"
#
# print(MyClass.i)
# print(MyClass.f)
# print(MyClass.__doc__)
# #
# # #Class attributes also support assignment
# MyClass.i=5000
# print(MyClass.i)

#Class instantiation
# class Complex:
#     def __init__(self,realpart,imagpart):
#         self.r=realpart
#         self.i=imagpart
#
#     def f(self):
#         return "Hello"
#
# x=Complex(3.0,-4.5)
# # print(x.r)
# # print(x.i)
# # print(x.f())
# #
# # # Class functions for attributes
# print(hasattr(x,'r'))
# print(getattr(x,'r'))
# print(setattr(x,'r',6.0))
# print(x.r)
# print(delattr(x,'r'))
# print(x.r)


#Explain self in detail
#Self in each calls the individual instances of the class
# class Apollo:
#
#     destination="moon"
#
#     def fly(self):
#         print("Spaceship is flying...")
#     def get_destination(self):
#         print("Destination is:",self.destination)
#
# #First object
# first=Apollo()
# #Second object
# second=Apollo()
# #
# #Lets change the destination for first
# first.destination="mars"
# first.fly()
# first.get_destination()
# #Calling second object
# second.fly()
# Apollo.destination="banana"
# second.get_destination()




#Object Initialization
# class Example:
#     def __init__(self,value1,value2):
#         self.myVariable1=value1
#         self.myVariable2=value2
#         print("All variables initialized")
#
# dummy=Example(2,3)
# print(dummy.myVariable1)
# print(dummy.myVariable2)









