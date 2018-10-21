#check for palindrome
a = input("Please enter your string sir/maam!!!")
print("Your string was fully checked element by element and it was found that it is",end=" ")
if(a!=a[::-1]):
    print("NOT",end="")
print(" a palindrome.")
