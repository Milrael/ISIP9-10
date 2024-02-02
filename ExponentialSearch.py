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

def ExponentialSearch(arr, element):
    if arr[0] == element:
        return 0
    index = 1
    while index < len(arr) and arr[index] < element:
        index = index * 2
    return BinarySearch( arr[:min(index, len(arr))], element)

arr = [1 ,5, 15, 65, 76, 195, 198, 210]
# arr2 = ['баобаб', 'ежик', 'зима', 'кролик', 'кукуруза', 'мороз', 'собака', 'шишка']
key = 201
# key2 = 'кукуруза'
# print(ExponentialSearch(arr, key))
# print(ExponentialSearch(arr2, key2))


Алгоритм выполняется следующим образом:
1)Определяется диапазон, в котором, скорее всего, будет находиться искомый элемент.
2)В этом диапазоне используется двоичный поиск для нахождения индекса элемента.