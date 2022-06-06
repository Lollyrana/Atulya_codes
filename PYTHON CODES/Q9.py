def str_ascend():
    x=input("Enter the string")
    y=[]
    for i in x:
        y.append(i)
    y.sort()
    y=''.join(y)
    print(y)
str_ascend()