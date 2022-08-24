# to find the arithmetic mean
#When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
#Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3

def arithmetic_mean(test_data):
    result = [0]
    mean = sum(test_data)/len(test_data)
    print(mean)

    for i in range(len(test_data)):
        if test_data[i] < mean:
            result.append(test_data[i])

    return result


result_returned=arithmetic_mean([1, 8,7,3, 5, 6, 4, 10, 2, 3,56])
print(result_returned)