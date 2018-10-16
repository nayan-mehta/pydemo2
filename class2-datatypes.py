#print statement and print()
# print(value, ..., sep=' ', end='\n', file=sys.stdout)

# a = 1.24
# print("a=", a)
# print("a = \n", a)


# print("a","b")
# print("a","b", sep='')
# print(192,168,178,42, sep='.')
# print("a","b", sep=':)')
#
# for i in range(4):
#     print(i)
#
# for i in range(4):
#     print(i, end=" ")

# fh = open("data.txt","w")
# print("Outputting data to file and not prompt", file=fh)
# fh.close()

# Data Types

#Integers (Teach functions also, bin(),oct(),hex())

# print(60)
# print(0b111100)
# print(0o74)
# print(0x3c)
#
# print(type(60))
# print(type(0o10))
# print(type(0x3c))

#Floating point

# print(4.2)
# print(type(4.2))
# print(4.)
# print(.4e7)
# print(4.2e-4)
# print(1.8e308)

#Complex number
# print(2+3j)
# print(type(2+3j))

#Strings
# print("Hello!!")
# print(type("Hello!!"))
# print('This string contains a single quote (\') character.')

#Escape Sequences in Strings
#powers stripped
# print("\\n")
# print("\\")
# print('a\
# b\
# c')

#Special powers
# print("a\tb")
# print("a\141\x61")
# print("a\nb")
# print('\u2192 \N{rightwards arrow}')
#Raw string
# print('foo\nbar')
# print(r'foo\nbar')
# print(R'foo\\bar')
#
# print('''This string has a single (') and a double (") quote.''')

#Bool

# print(type(True))
# print(type(False))

#Built-in Functions
# print(abs(-99.0002992))
# print(divmod(32,8))
# print(max(4,222,999))
# print(min(1,2,-99))
# print(pow(2,3))
# print(round(3.4455))
# print(sum([1,2]))

#Type conversions
# print(str(3)+"Hello")
# a = input()
# b = input()
# c = int(a)+int(b)
# print(c)
