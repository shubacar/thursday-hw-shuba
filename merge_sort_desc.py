#merge sort descending
def merge_sort(test_data):
   if len(test_data) <= 1:
       return test_data
   middle= len(test_data) // 2
   first=merge_sort(test_data[:middle])
   second=merge_sort(test_data[middle:])
   return merge_array(first,second)

def merge_array(left_arr, right_arr):
    merged_array = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_array.append(right_arr[j])
            j += 1
            continue

        if j == len(right_arr):
            merged_array.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] >= right_arr[j]:
            merged_array.append(left_arr[i])
            i += 1
        else:
            merged_array.append(right_arr[j])
            j += 1

    return merged_array


testarr = [1,3,6,2,4,9,7]
combined = merge_sort(testarr)
print(combined)