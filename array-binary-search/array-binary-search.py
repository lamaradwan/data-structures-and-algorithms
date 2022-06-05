def binary_search(arr,x):
    try:
        begin_index = 0
        end_index = len(arr)-1
        while begin_index <= end_index:
            mid = begin_index + (end_index - begin_index) // 2
            if x == arr[mid]:
                return mid
            elif x<arr[mid]:
                end_index = mid-1
            else:
                begin_index = mid+1
        return -1
    except TypeError:
        print(f"You have a {TypeError}, please enter a string")



print(binary_search([-131, -82, 0, 27, 42, 68, 179],42))
print(binary_search([-131, -82, 0, 27, 42, 68, 179],"42"))
print(binary_search([],42))
print(binary_search([2.04,5.60,10.45,1.98,8.89],5.60))
print(binary_search([1],1))