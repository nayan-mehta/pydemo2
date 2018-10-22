#if statement
# var1 = 10
# var2 = 12
#
# if var2 > var1:
#     print( var2,'is greater then', var1)
#
# if var2 < var1:
#     print(var2,'is equal', var1)

#if else
# var1 = 10
# var2 = 12
#
# if var2 > var1:
#     print( var2,'is greater then', var1)
# else:
#     print(var2,'is smaller then', var1)

#if elif

# age1 = 15
#
# if age1 < 12:
#     print('my age is ', age1)
# elif (age1 >= 12) and (age1 < 18):
#     print('my age is ', age1)
# else:
#     print('my age is ', age1)

#Printing ranges
# n=5
# for x in range(5):
#     print(x*n)

# for x in range(3,6):
#     print(x)
#
# for x in range(20,-5,-1):
#     print(x)



# fruits=['banana','apple','mango']
#
# for index in range(len(fruits)):
#     print("Current Fruit:",fruits[index])

#Iterating over a list

# l=['lala','beebee','boopboop']
#
# for i in l:
#     print(i)

#Iterating over a tuple(Immutable)

# t=('dumdum','deedee','doodoo')
# for i in t:
#     print(i)

#Iterating over a string

# s="Dumdeedum"
# for i in s:
#     print(i)

#Iterating over dictionary

# d={}
# d['xyz']=123
# d['abc']=345
#
# for i in d:
#     print("%s %d"%(i,d[i]))

# for letter in "python":
#     print("Current Letter: ",letter)


#While loop
# count=0
# while (count<9):
#     print("The count is: ",count)
#     count=count+1
#
# print("Goodbye!")

#Infinite Loop
# while True:
#     print("Hello")

# n = int(input("Enter a no : "))
# if n <= 0:
#     print("enter a valid no")
# else:
#     add = 0
#     while n > 0:
#         add += n
#         n -= 1
#
# print(add)

#break example

# while True:
#     s = input('Enter any string : ')
#     if s == 'quit':
#         break
#     print('Length of the string is', len(s))
# print('Game over')

# for letter in "Python":
#     if letter =='h':
#         break
#     print("Current letter:",letter)
#
# var =10
# while var>0:
#     print("Current value: ",var)
#     var=var-1
#     if var==5:
#         break
# print("Bye")

#continue example

# for letter in "Python":
#     if letter =='h':
#         continue
#     print("Current letter:",letter)

# var =10
# while var>0:
#     print("Current value: ",var)
#     var=var-1
#     if var==5:
#         continue
#     print("Hello")
# print("Bye")

#break and continue

# count=0
# while True:
#     print(count)
#     count+=1
#     if count>=5:
#         break

# for x in range(10):
#     if x%2==0:
#         continue
#     print(x)


#Nested loops- while example

# i=2
# while(i<100):
#     j=2
#     while(j<=(i/j)):
#         if not (i%j):break
#         j=j+1
#     if(j>i/j): print(i,"is a prime number")
#     i=i+1
# print("Bye")




# for i in range(10):
#     x = input("Enter an integer")
#     print(x)
#
# [1,2,4.5,"Hello"]
#



