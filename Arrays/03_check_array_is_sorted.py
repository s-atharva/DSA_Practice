my_arr = [1, 2, 2]


def check_array_is_sorted(arr):
    if len(arr) <= 1:
        return True
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

print(check_array_is_sorted(arr=my_arr))
