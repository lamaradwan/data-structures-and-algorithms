from quick_sort.quick_sort import quick_sort, partition

def test_sortion():
    arr = [8,3,2,4]
    quick_sort(arr,0,len(arr)-1)
    actual = arr
    expected = [2,3,4,8]
    assert actual == expected


def test_sorted_list():
    arr = [2, 3, 5, 7, 13, 11]
    quick_sort(arr, 0, len(arr) - 1)
    actual = arr
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected

def test_duplicated_values_list():
    arr = [5, 12, 7, 5, 5, 7]
    quick_sort(arr, 0, len(arr) - 1)
    actual = arr
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_negative_values_list():
    arr = [20, -18, 12, 8, 5, -2]
    quick_sort(arr, 0, len(arr) - 1)
    actual = arr
    expected = [-18, -2, 5, 8, 12, 20]
    assert actual == expected

def test_one_index():
    arr = [1]
    quick_sort(arr, 0, len(arr) - 1)
    actual = arr
    expected = [1]
    assert actual == expected

def test_empty_list():
    arr = []
    quick_sort(arr, 0, len(arr) - 1)
    actual = arr
    expected = []
    assert actual == expected