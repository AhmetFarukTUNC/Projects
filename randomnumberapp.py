import random
hak=int(input("Hak : "))
can =100
for i in range(hak):
    number = random.randint(1,100)
    value = int(input("Value : "))
    print(number)
    if number == value :
        can+=0
        print("Anlık Puan :",can)
    else:
        
        can=can-(can/hak)
        print("Anlık puan :",can)


