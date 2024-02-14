# We defined as 1 is summation,2 is substraction,3 is multiplication,4 is divide and 5 is exponention,Q is quit.


print("""

Welcome to Calculator Machine!!!
      
[1] summation
      
[2] subtraction
      
[3] multiplication
      
[4] divide
      
[5] exponentiation

[Q] Quit
      
""")

# We took input according options in top and assigned to operation variable.

operation = input("Please,input operation that you wanted do : ")

# if operation is 1,we takes values as number1 and number2.Finally,we print to summation of number1 and number2.

if operation == "1":

    number1 = float(input("PLease,input first number : "))

    number2 = float(input("Please,input second number : "))

    print("Result of summation operation is {}.".format(number1 + number2))

# if operation is 1,we takes values as number1 and number2.Finally,we print to screen  differential of number1 and number2. 

elif operation == "2":
      number1 = float(input("PLease,input first number : "))

      number2 = float(input("Please,input second number : "))

      print("Result of substraction operation is {}.".format(number1 - number2))

# if operation is 3,we took values as number1 and number2,finally printed result of multiplication operation for number1 and number2. 

elif operation == "3":
      number1 = float(input("PLease,input first number : "))

      number2 = float(input("Please,input second number : "))

      print("Result of multiplication operation is {}.".format(number1 * number2))
     
# if operation is 4,we took values as number1 and number2,after that,we printed result of divide operation for number1 and number2.
      
elif operation == "4":
      number1 = float(input("PLease,input first number : "))

      number2 = float(input("Please,input second number : "))

      print("Result of divide operation is {}.".format(number1 / number2))

# if operation is 5,we took values as number1 and number2,after that,we printed result of exponention operation for number1 and number2.     

elif operation == "5":
      number1 = float(input("PLease,input first number : "))

      number2 = float(input("Please,input second number : "))

      print("Result of exponentiation operation is {}.".format(number1**number2))

# if operation is Q or q we printed exiting expression.     

elif operation == "Q" or operation == "q":
      
      print("Exiting...")

