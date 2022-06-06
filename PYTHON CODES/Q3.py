def calculator():
    x=int(input("Enter first number:"))
    y=input("enter an operator:")
    z=int(input("enter second number:"))
    if y=='.':
        print(x*z)
    elif y=='/':
        print(x/z)
    elif y == '-':
        print(x - z)
    elif y == '+':
        print(x + z)
    else:
        print("enter a valid inputs\n")
        calculator()
while True:
    try:
        calculator()
        break
    except:print ("enter valid inputs\n")
