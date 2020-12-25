def merge_sort(array):
    if len(array) <= 1:
        return array

    array_length = len(array)
    midpoint = array_length // 2
    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])

    return merge(left, right)


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


## HEAP SORT GOES HERE##

# heapify takes 3 prameters: array, length of array n, index of parent node i

def heapify(array, n, i):
    largest = i
    left = right = (i * 2) + 1

    if left < n and array[left] > array[largest]:
        largest = 1
    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        heapify(array, n, largest)


def heap_sort(array):
    n = len(array)


## OTHER ALGORITHMS FOR SORTING GOES HERE


def main():
    my_arr = [5, 2, 7, 4]
    print(my_arr)

    new_arr = merge_sort(my_arr)
    print(new_arr)


main()
