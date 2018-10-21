Cap =0
i=int(input("length of string"))
a=input("anystring of i length")
for k in range (0,i):
    if(64<ord(a[k])&ord(a[k])<91):
       Cap=Cap+1
       print(a[k])
print("Number of Capital letter in string is : - ")
print(Cap)
