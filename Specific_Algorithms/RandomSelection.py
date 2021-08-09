# partition subroutine
def Partition(arr, left, right):
    pivot = arr[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[left], arr[i - 1] = arr[i - 1], arr[left]
    return arr.index(pivot)
# select an element of ith order statistic in an unsorted array of length N
def RandomSelection(arr, n, i, left, right):
    if n == 1:
        return arr[i]
    else: 
        j = Partition(arr, left, right)
        if j == i:
            return arr[j]
        elif j > i:
            return RandomSelection(arr, j - 1, i, left, j - 1)
        elif j < i:
            return RandomSelection(arr, n - j, i - j, j + 1, right)

print(RandomSelection([9, 7, 6, 5, 2, 1, 18], 7, 3, 0, 6)) 