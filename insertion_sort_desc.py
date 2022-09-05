#insertion sort

def insertion_sort(test_data):
    for i in range(1,len(test_data)):
        key=test_data[i]
        j = i-1
        while j >= 0 and key > test_data[j]:
             test_data[j+1] =test_data[j]
             j -= 1
        test_data[j+1]=key

    return test_data

test_data=[1,3,5,9,0,7]
result=insertion_sort (test_data)
print(result)