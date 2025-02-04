def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}


def calculator():
    calculating = True
    first = float(input("Whats the first number?: "))
    while calculating:
        for key in operations:
            print(key)
        operation = input("Pick an operation: ")
        next = float(input("Whats the next number?: "))
        answer = operations[operation](first,next)
        print(f"{first} {operation} {next} = {answer}")

        continue_calc = input(f"Type 'y' to continue with {answer}, type 'n' to start new.")
        if continue_calc == 'n':
            calculating = False
            print("\n" *20)
            calculator()
        elif continue_calc =='y':
            first = answer

calculator()