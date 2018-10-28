#Inheritance

# Parent class
# class Parent:
#     a=10
#     b=1000
#     def doThis(self):
#         print("Do this")
#     def doThat(self):
#         print("Do That")
#
# #Child class inheriting Parent class
# class Child(Parent):
#     #child variables
#     a=100
#     b=1000
#     def doWhat(self):
#         print("Do What")
#     def doNotDoThat(self):
#         print("Do not do that")
#
# parentobj=Parent()
# childobj=Child()
# childobj.doThis()
# childobj.doWhat()
#
# parentobj.doWhat()

#Animals- mammal and amphibians
# class Animal:
#
#     multicellular=True
#     eukaryotic=True
#
#     def breathe(self):
#         print("Breathing")
#     def feed(self):
#         print("Feeding")
#
# class Mammal(Animal):
#
#     haveMammaryGland=True
#     WarmBlood=True
#
#     def produceMilk(self):
#         print("Produce Milk")
#
# class Amphibian(Animal):
#
#     liveInWater=True
#
#     def metamorphosis(self):
#         print("Metamorphosis")
# Frog=Amphibian()
# Frog.breathe()
# Frog.metamorphosis()
# print(Frog.liveInWater)
#
# Dolphin=Mammal()
# Dolphin.produceMilk()


#Multiple Inheritance
# class A:
#     a=100
# class B:
#     b=200
# class C(A,B):
#     c=300
# c_obj=C()
# print(c_obj.a)
# print(c_obj.b)
# a_obj=A()
# print(a_obj.c)


#Multi-level Inheritance
# class A:
#     a=100
# class B(A):
#     b=200
# class C(B):
#     c=300
# a_obj=A()
# b_obj=B()
# c_obj=C()
# print(a_obj.a)
# print(b_obj.a)
# print(c_obj.a)

#Overriding

# class Parent:        # define parent class
#    def myMethod(self):
#       print ('Calling parent method')
#
# class Child(Parent): # define child class
#    def myMethod(self):
#       print ('Calling child method')
#
# c = Child()          # instance of child
# c.myMethod()         # child calls overridden method

#Overloading operators

# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)
#
#
# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print(v1 + v2)

#Data Hiding

# class JustCounter:
#     a = 10
#     __secretCount = 0
#
#     def count(self):
#         self.__secretCount += 1
#         print(self.__secretCount)
#
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.a)
# print(counter.__secretCount)
# print(counter._JustCounter__secretCount)


#Encapsulation

# class Car:
#     def __init__(self):
#         self.__updateSoftware
#     def drive(self):
#         print('Driving')
#     def __updateSoftware(self):
#         print('Updating Software')
# redcar=Car()
# redcar.drive()
# # redcar.__updateSoftware()
# redcar._Car__updateSoftware()

#Dicts
#Iteration multiple
# sammy = {'username': 'sammy-shark', 'online': True, 'followers': 987}
# jesse = {'username': 'JOctopus', 'online': False, 'points': 723}
#
# for common_key in sammy.keys() & jesse.keys():
#     print(sammy[common_key], jesse[common_key])
# #
# sammy = {'username': 'sammy-shark', 'online': True, 'followers': 987}
#
# print(sammy.values())
#
# for key, value in sammy.items():
#     print(key, 'is the key for the value', value)

#Modifying
# usernames = {'Sammy': 'sammy-shark', 'Jamie': 'mantisshrimp54'}
# usernames['Drew'] = 'squidly'
# print(usernames)

#Delete
# #
# jesse = {'username': 'JOctopus', 'online': False, 'points': 723, 'followers': 481}
# del jesse['points']
# print(jesse)
#
#
# jesse = {'username': 'JOctopus', 'online': False, 'points': 723, 'followers': 481}
# jesse.clear()
# print(jesse)



















