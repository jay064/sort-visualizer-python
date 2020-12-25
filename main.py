def main():

    # FOR TESTING PURPOSES

    my_arr = [5, 2, 7, 4]
    print(my_arr)

    new_arr_merge = merge_sort(my_arr)
    new_arr_heap = heap_sort(my_arr)

    print(new_arr_merge)
    print(new_arr_heap)


main()


# MERGE SORT GOES HERE

def merge(left, right):
    sorted_array = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1

        else:
            sorted_array.append(right[right_index])
            right_index += 1

    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])

    return sorted_array


def merge_sort(array):
    if len(array) <= 1:
        return array

    array_length = len(array)
    midpoint = array_length // 2
    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])

    return merge(left, right)


# HEAP SORT GOES HERE##

# heapify takes 3 parameters: array, length of array n, index of parent node i

def heapify(array, n, i):
    largest = i
    left = (i * 2) + 1
    right = (i * 2) + 2

    if left < n and array[left] > array[largest]:
        largest = 1
    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        heapify(array, n, largest)


def heap_sort(array):
    sorted_array = []
    n = len(array)
    last = int(n / 2) - 1
    first = -1
    for i in range(last, first, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    sorted_array = array
    return sorted_array

## OTHER ALGORITHMS FOR SORTING GOES HERE
