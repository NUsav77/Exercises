def minimumSwaps(arr):
    sorted_array = sorted(arr)
    num_swaps = 0
    temp_dict = {elem: i+1 for i, elem in enumerate(sorted_array)}
    for i, elem in enumerate(arr):
        val = sorted_array[i]
        if elem != val:
            temp = arr[i]
            arr[temp-1] = temp
            arr[i] = sorted_array[i]
            num_swaps += 1

    return num_swaps


array = [7, 1, 3, 2, 4, 5, 6]
minimumSwaps(array)
