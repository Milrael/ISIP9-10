import math
import time

def JumpSearch(arr, element):
    length = len(arr)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and arr[left] <= element:
        right = min(length - 1, left + jump)
        if arr[left] <= element and arr[right] >= element:
            break
        left += jump
    if left >= length or arr[left] > element:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and arr[i] <= element:
        if arr[i] == element:
            return i
        i += 1
    return -1

arr = [1 ,5, 15, 65, 76, 195, 198, 210, 299]
print(JumpSearch(arr, 121))

# element = 195
# left = 0
# jump = 3
# length = 9
# right = 3

Интерполяционный поиск