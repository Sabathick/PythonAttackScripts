def sum(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y

print("Select operation:")
print("1-Sum")
print("2-Subtraction")
print("3-Multiplication")
print("4-Division")

while True:
    choice = input("Select a operation:(1,2,3,4):")
    if choice in ('1','2','3','4'):
        num1 = float(input("Type the first number:"))
        num2 = float(input("Type the second number:"))

    if choice == '1':
        print(num1,"+",num2,"=",sum(num1,num2))
    elif choice == '2': 
        print(num1,"-",num2,"=",subtract(num1,num2))
    elif choice == '3': 
        print(num1,"*",num2,"=",multiply(num1,num2))
    elif choice == '4': 
        print(num1,"/",num2,"=",division(num1,num2))
    next = input("Let's do next calculation?(yes/no)")
    if next == 'no':
        break
else:
    print("Invalid input")
