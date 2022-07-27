def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left,right)


def merge_two_sorted_lists(arr1, arr2):
    sorted_list = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            sorted_list.append(arr1[i])
            i += 1
        else:
            sorted_list.append(arr2[j])
            j += 1

    while i < len(arr1):
        sorted_list.append(arr1[i])
        i += 1

    while j < len(arr2):
        sorted_list.append(arr2[j])
        j += 1

    return sorted_list


if __name__ == '__main__':
    print(merge_sort([3,5,9,1,2,4]))
    # [3,10,5,9,1,2,7,4]
