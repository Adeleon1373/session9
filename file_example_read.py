fp = open("text.txt","r")
print(fp.read())
fp.close() # not needed in this example

#same thing but more pythonic
with open("text.txt","r") as fp: #this creates a context
    print(fp.read())

print("we are done, the context is closed by the indent")

#read from the same file, line by line
with open("text.txt","r") as fp:
    line_number = 1
    for line in fp:
        #print(line, end="")
        print(f"{line_number}:{line.rstrip()}")
        line_number += 1
