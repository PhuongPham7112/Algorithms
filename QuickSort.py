def Partition(arr, left, right):
    pivot = arr[left]
    i = left + 1
    for j in range(left + 1, right + 1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[left], arr[i - 1] = arr[i - 1], arr[left]
    return arr.index(pivot)
    
def QuickSort(arr, length, left, right):
    if left < right:
        pivot = Partition(arr, left, right)
        QuickSort(arr, len(arr), left, pivot - 1)
        QuickSort(arr, len(arr), pivot + 1, right)
        print(arr)

my_list = [2, 3, 5, 7, 1, 9, 12, 4]
print(Partition(my_list, 0, len(my_list) - 1))
QuickSort(my_list, len(my_list), 0, len(my_list) - 1)