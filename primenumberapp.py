operationnumber=int(input("Operation Number : "))
firstoperation = 1
while firstoperation<=operationnumber:
    sayi=int(input("input number : "))
    if sayi > 1:
    
        for i in range(2,sayi):
            if (sayi % i) == 0:
                print(sayi,"Not prime number.")
                break
        else:
            print(sayi," Prime number.")
 
    else:
       print(sayi," Not prime number.")
    firstoperation+=1

            
    
