def Fibonacci(lys, element):
    fibm_1 = 0
    fibm_2 = 1
    fibm = fibm_1 + fibm_2
    while(fibm < len(lys)):
        fibm_2 = fibm_1
        fibm_1 = fibm
        fibm = fibm_1 + fibm_2
    index = -1
    while (fibm > 1):
        q = min(index + fibm_2, (len(lys)-1))
        if (lys[q] < element):
            fibm = fibm_1
            fibm_1 = fibm_2
            fibm_2 = fibm - fibm_1
            index = q
        elif (lys[q] > element):
            fibm = fibm_2
            fibm_1 = fibm_1 - fibm_2
            fibm_2 = fibm - fibm_1
        else:
            return q 
    if(fibm_1 and index < (len(lys)-1) and lys [index+1] == element):
        return index+1
    return -1  
arr = [1,3,8,11,19,31,44,63,120]
print(Fibonacci(arr,63))      