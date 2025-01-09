# 0 -> a <= b
# 1 -> a > b
#script to lexicographically sort a list of tuples with variable tuple sizes without using inbuilt function
def comp(a, b):
    i, j = 0, 0
    n, m = len(a), len(b)
    while(i< n and j < m):
        if a[i] < b[j]:
            return 0
        elif a[i] > b[i]:
            return 1
        i+= 1
        j+= 1
        
    if len(a) < len(b):
        return 0
    elif len(a) > len(b):
        return 1
    return 0

def mergeSortedArrays(s1, s2):
    s = []
    n, m = len(s1), len(s2)
    i, j = 0, 0
    while(i < n or j < m):
        a = s1[i] if i < n else (float("inf"),)
        b = s2[j] if j < m else (float("inf"),)
        if comp(a, b) == 0:
            s.append(a)
            i += 1
        else:
            s.append(b)
            j+= 1
    return s
    
def mergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr 
    mid = n//2
    s1, s2 = mergeSort(arr[:mid]), mergeSort(arr[mid:])
    s = mergeSortedArrays(s1, s2)
    return s
    
if __name__ == "main":
    testArray = [    (32, 49),    (32, 14, 39),    (31, 49, 47, 36, 44),    (48,),    (37, 36, 35),    (19, 31, 22, 10, 29),    (28, 24),    (25, 3),    (45, 16, 33, 20, 25),    (42, 40, 17),    (5, 1, 7, 3),    (3, 26, 37),    (2, 16, 10),    (22, 27),    (31, 39)]
    sorted_arr = mergeSort(testArray)
    print(sorted_arr)