#defines the equation and returns the sum of the two numbers
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#prompts the user to choose if they would either load the calculator or open the file.
while True:
    
    prompt = input("Would you like to open 'OutputFile' file or calculator: \n").lower()
#error handeling if the user inputs a spelling mistake, returns to the question asked in the previous line
    if prompt not in ['outputfile', 'calculator']:
        print("Invalid input. Please enter either 'OutputFile' or 'Calculator.\n")
        continue
    break 
#if the user chooses to open file, the file is then opened as read only and printed in consol
if prompt == "outputfile":
    try:
        with open('OutputFile.txt', 'r') as f:
            data = f.read()
            print(data)
#error handeling incase the file is not found, prompts the user to try again.    
    except FileNotFoundError as error:
        print("The file you are looking for does not exist \n")
        print("please use calculator")
        print(error)
#if the user chose calculator, it will open/create writing in the results outputed.
elif prompt == 'calculator':
    try:
        with open('OutputFile.txt', 'w') as f:
            #the user is given choices of operations to pick and choose from
            print("Select operation.")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
    
            while True:
                try:
            #depending on the number they input the code will run the respective calculation after the number for the calculations are input in the next line
                    choice = int(input("Enter choice (1/2/3/4): "))
                    if choice in [1, 2, 3, 4]:
                        f.write(f"Choice: {choice}\n")
                        break
                    else:
                        print("Invalid choice. Please enter a number from 1 to 4.")
            #error handeling incase the user inputs anything other that 1 to 4
                except ValueError:
                    print("Invalid choice. Please enter a number from 1 to 4.")

            while True:
                try:
            #prompt requiring the user to enter the first number to the calculation.
                    num1 = float(input("Enter first number: "))
                    f.write(f"First number: {num1}\n")
                    break
            #error handeling incase the user inputs anything other that 1 to 4
                except ValueError:
                    print("Invalid input. Please enter a number.")

            while True:
                try:
            #prompt requiring the user to enter the second number to the calculation.
                    num2 = float(input("Enter second number: "))
                    f.write(f"Second number: {num2}\n")
                    break
            #error handeling incase the user inputs anything other that 1 to 4
                except ValueError:
                    print("Invalid input. Please enter a number.")
#depending on the number chosen by the user 1-4 the equation is then ran. using the f.write, the calculation output is saved to the .txt file.
            if choice == 1:
                result = add(num1, num2)
                f.write(f"{num1} + {num2} = {result}\n")
                print(f"{num1} + {num2} = {result}\n")

            elif choice == 2:
                result = subtract(num1, num2)
                f.write(f"{num1} - {num2} = {result}\n")
                print(f"{num1} - {num2} = {result}\n")

            elif choice == 3:
                result = multiply(num1, num2)
                f.write(f"{num1} * {num2} = {result}\n")
                print(f"{num1} * {num2} = {result}\n")

            elif choice == 4:
                result = divide(num1, num2)
                f.write(f"{num1} / {num2} ={result}\n")
                print(f"{num1} / {num2} ={result}\n")
#error handeling incase user enters a number equal to zero in the division choice.
    except ZeroDivisionError:
         print("Error: division by zero")

