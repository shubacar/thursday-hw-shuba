#When given a list of elements, find the two lowest elements.
#They can be equal to each other or different.
#Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def find_lowest(test_data):
    test_data.sort()
    res = [ test_data[0], test_data[1] ]
    print(res)

test_data=[0,2,1,5,0,8,9]
find_lowest(test_data)

