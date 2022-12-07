mylist = []
msg = ""
while msg != 'stop'.upper():
    msg = input("Enter new item, and STOP to finish\n")
    mylist.append(msg)
print(mylist)