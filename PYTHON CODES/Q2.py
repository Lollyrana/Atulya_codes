def credi():
    while True:
            ccn=input("Enter the credit card number\n")
            if (len(ccn)==16):
                break
            else:
                print("Enter a valid input\n")
    s="************"
    for i in range(0,4):
        s=s+str(ccn[i+12])
    print(s)
credi()
