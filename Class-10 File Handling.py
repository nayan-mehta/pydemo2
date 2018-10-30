# f=open('demo.txt')
# f=open('/Users/nayanmehta/Desktop/dummy/pydemo2/demo.txt')
#
# f=open('lalalala.txt','r')
# f=open('lalalal.txt','w')


# file=open('demo.txt','r')
# # print(file.read(10))
# print(file.read())

# file = open('demo.txt', 'r')
# print(file.readline())
# print(file.readline())

# file = open('demo.txt', 'r')
# print(file.readlines())

#Loop over method

# file = open('demo.txt', 'r')
# for line in file:
#     print(line)

# file = open('testfile.txt', 'w')
# file.write('This is a test\n')
# file.write('hello hello')

# file= open('testfile.txt','w')
# lines_of_text = ['One line of text here\n', 'and another line here\n', 'and yet another here\n',
#                                 'and so on and so forth']
# file.writelines(lines_of_text)

# file = open('testfile.txt', 'r')
# print(file.read())
# file.close()

#Append
# file = open('testfile.txt', 'a')
# file.write('\nhello hello')
# file.close()

#x mode
# file = open('helooo.txt', 'x')

#Open a file
# f=open('demo.txt','r+')
# data=f.read(19)
# print('Read string is:',data)
#
# #Check current position
# position=f.tell()
# print('Current file position:',position)
# print(f.read(10))
# position=f.tell()
# print('Current file position:',position)
#
# # #Repostion to the start
# postion=f.seek(10,0)
# data=f.read(19)
# print('Again read the string: ',data)
#
# f.close()


#with to open files

# with open('demo.txt') as f:
#     for line in f:
#         print(line)



import os

# os.rename('demo.txt','dementor.txt')
#
# os.remove('dementor.txt')


# with open('hello1.txt', 'r') as f:
#     data = f.readlines()
#     print(data)
#     for line in data:
#         words = line.split()
#         print(words)








