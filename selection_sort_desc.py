# given an unsorted list sort them using selection sort

def selection_sort(test_data):

    for i in range(0,len(test_data)):
        min_index= i
        for j in range(i+1,len(test_data)):
            if test_data[j] > test_data[min_index]:
                min_index = j
        test_data[i],test_data[min_index]=test_data[min_index],test_data[i]

    return test_data

test_data=[1,3,4,6,2,5]
print(selection_sort(test_data))