import art


def add(n1, n2):
    return n1 + n2

# TODO: write out the other 3 functions for subtraction, multiplication and division

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

# TODO: Add these 4 functions in a dictionary as values for Keys: '+','-','*','/'

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#TODO 3:use the dictionary operations to perform calculations

def calculator():
    print(art.logo)
    first_num = float(input("enter the first number: "))
    result = ""
    to_continue = True

    while to_continue:
        for symbol in operations:
            print(symbol)

        choose_operator = input("type a mathematical operator: ")
        second_num = float(input("enter the second number: "))
        result = operations[choose_operator](first_num,second_num)
        print(f"{first_num} {choose_operator} {second_num} = {result}")
        user_wish = input("you want want to continue with same calculation type 'yes' or to start a new calculation 'no': ")
        if user_wish == "no":
            to_continue = False
            print("\n"*20)
            calculator()
        elif user_wish == "yes":
            first_num = result
        else:
            print("invalid input - so exiting...")
            return
calculator()

