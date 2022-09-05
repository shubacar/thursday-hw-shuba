def bubble_sort(test_data):
    for i in range (len(test_data)):
        for j in range (len(test_data) - 1 -i):
            if test_data[j] < test_data[j+1]:
                test_data[j],test_data[j+1]=test_data[j+1],test_data[j]

    return test_data


test_data = [1,3,8,7,2,4,6,9]
print(bubble_sort(test_data))