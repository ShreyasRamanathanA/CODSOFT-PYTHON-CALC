#This project is to create a calculator to perform simple arithmetic operations
#This can perform +,-,*,/ on both integers and decimals

def calculator():
    print("\nSimple Calculator")
    while True:
        print("\nOperations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit(x)")

        operation = input("\nEnter operation number (+ or - or * or / or x): ")

        if operation == 'x':   #exit the program
            print("\nExiting the calculator...\n")
            break
        
        if operation not in ["+", "-", "*", "/"]:    #check for valid operation
            print("\nInvalid operation. Please try again!")
            continue
        
        #to handle ValueError
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("\nInvalid input. Please enter a valid number!")
            continue

        if operation == "+":   #add 2 numbers
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif operation == "-":   #subtract 2 numbers
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif operation == "*":   #multiply 2 numbers
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
        elif operation == "/":   #divide 2 numbers
            if num2 == 0:   #to handle ZeroDivisionError
                print("\nDivision by zero is not allowed.")
                continue
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")

calculator()   #run the program
