print("=========== Open a file =============")
#  Open a file

f = open("test.txt")    # open file in current directory
f = open("C:/Python27/README.txt")  # specifying full path

f = open("test.txt")      # equivalent to 'r' or 'rt' (read and read_text)
f = open("test.txt",'w')  # write in text mode
# f = open("img.bmp",'r+b') # read and write in binary mode

f = open("test.txt",mode = 'r',encoding = 'utf-8')

f.close()

print("=========== Write into a file =============")
# write into a file

with open("test.txt",'w',encoding = 'utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n")
    f.write("contains three lines\n")
    f.close()

print("=========== Read from a file =============")
# read from a file

f = open("test.txt",'r',encoding = 'utf-8')
data = f.read(8)    # read the first 8 data
print(data)

data = f.read(4)    # read the next 4 data
print(data)

data = f.read()     # read in the rest till end of file
print(data)

data = f.read()  # further reading returns empty sting
print(data)

f = open("test.txt",'r',encoding = 'utf-8')
data = f.read()  # further reading returns empty sting
print(data)

#  Read file line by line

f = open("test.txt",'r',encoding = 'utf-8')
for line in f:
    print(line, end = '')

print("=========== readlines() reads untill a new line character is found =============")

f = open("test.txt",'r',encoding = 'utf-8')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())