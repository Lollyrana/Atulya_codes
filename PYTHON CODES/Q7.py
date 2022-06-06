def most_frequency(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num
 
List = [2, 1, 1, 1, 1, 3]
print(most_frequency(List))