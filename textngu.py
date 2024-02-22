f = open("data.txt", "w+")
txt = "This is 1st line\n"
f.writelines(txt)
seq = " This is 2nd line\nThis is 3rd line"
f.seek(0, 2)
f.writelines(seq)
myList = []
for line in f:
    myList.append(line)
print(myList)
f.close()

x = [1, 2, 3]
y = x
x.append(4)
y = y + [5]
print(y)
