my_array = [1, 1, 2, 2, 2, 3, 3, 4]


def remove_duplicate_from_sorted_array(arr):
    my_set = set()
    # O(N log(N))
    for i in range(len(arr)):
        my_set.add(arr[i])
    arr_index = 0
    for elem in my_set:
        arr[arr_index] = elem
        arr_index += 1
    print(arr)

remove_duplicate_from_sorted_array(arr=my_array)
