#Your input is a list of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input list).
#Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def even_first(test_data):
    j = len(test_data)-1
    i=0
    while i < j:
        if test_data[i] % 2 == 0:
            i += 1
        else:
            test_data[j],test_data[i] = test_data[i],test_data[j]
            j -= 1



    print(test_data)


test_data=[7, 3, 5, 6, 4, 10, 3, 2]
#test_data=[1,3,1,2,4,5]
even_first(test_data)
