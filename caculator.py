def addition(num1,num2):
    result = num1 + num2
    print("{0} + {1} = {2}" .format(num1,num2,result))

def subtraction(num1,num2):
    result = num1 - num2
    print("{0} - {1} = {2}" .format(num1,num2,result))
    
def multipliction(num1,num2):
    result = num1 * num2
    print("{0} * {1} = {2}" .format(num1,num2,result))
    
def division(num1,num2):
    if num2 == 0.0:
        print("cant do divide by zero")
    else:
         result = num1 / num2
         print("{0} / {1} = {2}" .format(num1,num2,result)) 

while True:
    print("What do u want to do?")
    print("1 Addition")
    print("2 subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("Enter Q or q to Exit")

    choice = input("Enter the choice :")

    if choice == 'Q' or choice == 'q':
        break

    
    num1 = float(input("Enter number 1 :"))    
    num2 = float(input("Enter number 2 :")) 

    if choice == '1':
        addition(num1,num2)
    elif choice == '2':
        subtraction(num1,num2)
    elif choice == '3':
        multipliction (num1,num2)
    elif choice == '4':
        division(num1,num2)
    else:
         print("Invalid choice")
         print("\n")

