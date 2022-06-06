def srn_sum():
    a=input("Enter the string")
    b=0
    for i in a:
        try:
            b=b+int(i)
        except:
            pass
    print(b)
srn_sum()