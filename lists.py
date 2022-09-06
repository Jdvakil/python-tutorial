#Lists
mylist = ["one", "two", "three"]
print(mylist)

for i in mylist:
    print(i)

if "to" in mylist:
    print("yes")
else:
    print("no")

print(len(mylist))

mylist.append("four")
print(mylist)

mylist.insert(0,"zero")
print(mylist)

print(mylist.pop())

mylist.remove("three")
print(mylist)

mylist.sort()
print(mylist)

mylist2 = [1,2,3,4,5,6]
a = mylist2[0:-2:3]
print(a)