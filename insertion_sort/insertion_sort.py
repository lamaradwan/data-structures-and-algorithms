def insertion_sort(arr):
    if len(arr) == 0:
        return 'Empty List'

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == '__main__':
    # print(insertionSort([8,3,2,4]))
    # Insertion sort
    arr1 = [8,3,2,4]
    print(insertion_sort(arr1))
    print(insertion_sort([20, 18, 12, 8, 5, -2]))
    print(insertion_sort([5, 12, 7, 5, 5, 7]))
    print(insertion_sort([2, 3, 5, 7, 13, 11]))
    print(insertion_sort([]))
