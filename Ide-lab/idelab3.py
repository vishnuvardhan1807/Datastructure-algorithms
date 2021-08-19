class calc:
    def __init__(self, a ,b , c):
        self.a = a
        self.b = b
        self.c = c
    def simple_calculator(self):
        if operation == "+":
            print(int(first_number) + int(second_number))
        elif operation == "-":
            print(int(first_number) - int(second_number))
        elif operation == "*":
            print(int(first_number) * int(second_number))
        elif operation == "/":
            print(int(first_number) / int(second_number))
        else:
            print("Invalid operation")
            

if __name__=='__main__':
    print("Welcome to simple calculator")
    print("Please enter your first number")
    first_number = input()
    print("Please enter your second number")
    second_number = input()
    print("Please enter your operation")
    operation = input()
    ob = calc(first_number, second_number, operation)
    ob.simple_calculator()