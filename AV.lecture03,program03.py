t = 0
import time
#python practice
a = int(input("your acount balance to be entered! "))
print(a)
b = int(input("Your marks in Maths!"))
print(b)
c = int(input("No of holidays in this month you get!"))
print(c)
print("your wish is being processed")
for t in range (0,5):
    time.sleep(30)
    print(".",end=" ")
print("Thanks for your patience!!!!!!")
