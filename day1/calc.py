# project2

def add(x,y): return x + y
def subtract(x,y): return x - y
def multiply(x,y): return x * y
def divide(x,y): return x / y if y!=0 else "Error: Division by Zero!"

while True:
    op=input("Choose Operation + - * / or 'q' for quit : ")
    if op=='q' : break
    try:
        a = float(input("Enter a number : "))
        b = float(input("Enter second number : "))
        if op=='+': print("Result is : ",add(a,b))
        elif op=='-': print("Result is : ",subtract(a,b))
        elif op=='*': print("Result is : ",multiply(a,b))
        elif op=='/': print("Result is : ",divide(a,b))
        else: print("Invalid Operation.")
    except ValueError:
        print("Please Enter valid Number.")