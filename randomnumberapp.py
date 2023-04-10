import random
right=int(input("Hak : "))
heart =100
for i in range(right):
    number = random.randint(1,100)
    value = int(input("Value : "))
    print(number)
    if number == value :
        heart+=0
        print("at the moment point :",heart)
    else:
        
        heart=heart-(heart/right)
        print("at the moment point :",hearth)


