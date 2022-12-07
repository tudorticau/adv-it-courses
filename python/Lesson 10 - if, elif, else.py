age = 7

if (age <= 4):
    print("You are baby!")
elif (age > 4) and (age < 12):
    print("You are kid")
elif (age >= 12) and (age < 19):
    print("You are teenager")
else:
    print("You are old!")

print("---- END -----")

print("===========Compare if element from first array is in the second============")
all_cars = ['chrusler',  'dacia' ,'bmw', 'Kia' , 'vw' ,'seat', 'skoda' , 'lada', ' audi ' , 'ford' , ' Chevrolet' ]
german_cars = ['bmw', 'vw' , 'audi']

for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + " is German Car")