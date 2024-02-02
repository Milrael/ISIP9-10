def InsertionSort(lyst):
    for i in range(1, len(lyst)):
        item_to_insert = nums[i] 
        j = i - 1 #индекс предыдущего элемента
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j] 
            j -= 1  
        nums[j + 1] = item_to_insert
    return nums
      
nums = [27, 31, 15, 68, 6, 11, 3] 
print(InsertionSort(nums))

