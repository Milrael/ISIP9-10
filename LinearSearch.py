
def LinearSearch(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1



arr = [5, 15, 65, 76, 4 ,195, 198, 210]
print(f"Элемент с индексом {LinearSearch(arr, 4)}")
