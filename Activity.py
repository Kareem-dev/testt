
# Receives the inputs

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
print("Enter the operation you want to perform ")
print("Options: Add, Subtract, Multiply, Divide")
print("Or: A, S, M, D")
operator = input("Or: +, -, *, /: ").lower() 

def evenOrOdd(x):  # to check if the result is even or odd
    if x % 2 == 0:
        return "even"
    else:
        return "odd"

def calculate(x, y, op): 
    
    # Checks the types of the inputs    
    if (isinstance(x, int) and isinstance(y, int) and isinstance(op, str)) != True:
        return None
    
    # Performs the calculations
    
    elif (op == "a") or (op == "add") or (op == "+"):
        result = x + y
        output = "The result is: " + str(result) + ", and it is " + evenOrOdd(result) 
        return output

    elif (op == "s") or (op == "subtract") or (op == "-"):
        result = x - y
        output = "The result is: " + str(result) + ", and it is " + evenOrOdd(result) 
        return output

    elif (op == "m") or (op == "multiply") or (op == "*"):
        result = x * y
        output = "The result is: " + str(result) + ", and it is " + evenOrOdd(result) 
        return output

    elif (op == "d") or (op == "divide") or (op == "/"):
        result = x / y
        output = "The result is: " + str(result) + ", and it is " + evenOrOdd(result) 
        return output
    
# Prints the results
print(calculate(num1, num2, operator))
