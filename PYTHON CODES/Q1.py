def func():
    while True:

        try:
            l1=list(map(int,input("Enter all elements of list with space between them\n").split()))
            break
        except:
            print("enter a valid input\n")

    def rec():
        s=(input("Enter a command : 'ascending','descending ' or 'none'\n"))
        if s=="ascending":
            l1.sort()
        elif s=="descending" :
            l1.sort(reverse=True)
        elif s=="none":
            pass
            
        
        else :
            print("Enter a valid command")
            rec()
    rec()
    print("The List is now:"+str(l1))
func()