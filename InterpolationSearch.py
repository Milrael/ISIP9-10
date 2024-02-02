# Интерполяционный поиск

# arr
# element
# index
# start
# end
#
# index = start + [(element - arr[start]) * (end - start) / (arr[end] - arr[start])]

def InterpolationSearch(arr, element):
    start = 0
    end = len(arr) - 1
    while start <= end and element >= arr[start] and element <= arr[end]:
        index = start + int(((float(end - start) / (arr[end] - arr[start])) * (element - arr[start])))
        if arr[index] == element:
            return index
        if arr[index] < element:
            start = index + 1
        else:
            end = index - 1
    return -1

arr = [1 ,5, 15, 65, 76, 195, 198, 210]
key = 65

print(InterpolationSearch(arr, key))