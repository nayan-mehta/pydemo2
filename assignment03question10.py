
#question number 10
strinG =input("enter your mobile number>>>")
kp=strinG.isalnum()
print("We checked if the string",end=" ")
print(strinG,end=" ")
print("contain all Numeric Values and it does",end=" ")
if(kp==True):
    print("contain all numeric values.")
else:
    print("Not Contain all numeric values.")

