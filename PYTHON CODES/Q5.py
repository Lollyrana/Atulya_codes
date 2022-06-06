def duplicate():
    try:
        a=list(map(int,input("Enter the integer elements of the array with blank spaces between them\n").split()))
    except:
        print("Enter a valid input")
        duplicate()
    a.sort()
    c=0
    k=0
    while((k+c)<(len(a)-1)):

        if a[k+c]==a[k+c+1]:
            print(str(a[k+c])+" Repeats itself\n")
            k=k+1
        else:
            pass
        c=c+1
duplicate()