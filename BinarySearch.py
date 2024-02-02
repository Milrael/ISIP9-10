def BinarySearch(arr, element):
    first = 0
    last = len(arr) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if arr[mid] == element:
            index = mid
        else:
            if element < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index

arr = [1 ,5, 15, 65, 76, 195, 198, 210]
print(BinarySearch(arr, 195))

