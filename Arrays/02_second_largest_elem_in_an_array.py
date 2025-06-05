def find_second_largest_elem(my_array):
    if len(my_array) < 2:
        return "Second largest element is not found"

    sorted_array = sorted(my_array, reverse=True)
    # [7, 7, 5, 4, 2, 1]
    for i in range(1, len(sorted_array)):
        if sorted_array[i] < sorted_array[0]:
            return sorted_array[i]

    return "Second largest element is not found"

def find_second_largest_elem_better(my_array):
    if len(my_array) < 2:
        return "Second largest element is not found"
    # without sorted_array
    largest_element = my_array[0]
    for i in range(1, len(my_array)):
        if my_array[i] > largest_element:
            largest_element = my_array[i]
    second_largest_element = -1
    for i in range(len(my_array)):
        if my_array[i] > second_largest_element and my_array[i] < largest_element:
            second_largest_element = my_array[i]
    return second_largest_element



arr = [1, 2, 4, 7, 7, 5]
print(find_second_largest_elem(my_array=arr))
print(find_second_largest_elem_better(my_array=arr))