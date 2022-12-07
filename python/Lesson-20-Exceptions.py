import sys

filename = "Lesson 9 - Lists2.pi"

while True:
    try:
        print("Inside try")
        myfile = open(filename, mode='r', encoding="Latin-1")
    except Exception:
        print("Inside except")
        print("Error found!")
        print(sys.exc_info())
        filename = input("Enter correct file name! :")
    else:
        print("Inside ELSE")
        print(myfile.read())
        sys.exit()

print("============EOF===========")