def Merge(array, low, mid, high):
    # Make copies of both arrays we're trying to merge
    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = array[low:mid + 1]
    right_copy = array[mid+1: high + 1]

    # Initial values for variables that we use to keep
    # track of where we are in each array
    i = 0
    j = 0
    k = low

    while i < len(left_copy) and j < len(right_copy):
        if left_copy[i] < right_copy[j]:
            array[k] = left_copy[i]
            i += 1
        elif right_copy[j] < left_copy[i]:
            array[k] = right_copy[j]
            j += 1
        k += 1
    
    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while i < len(left_copy):
        array[k] = left_copy[i]
        k += 1
        i += 1
    
    while j < len(right_copy):
        array[k] = right_copy[j]
        k += 1
        j += 1
    

def MergeSort(array, low, high):
    # this one returns nothing, it just alters the state of the array or you could add the return thingy tooo
    if high > low:
        mid = ((high) + low)//2
        MergeSort(array, low, mid)
        MergeSort(array, mid + 1, high)
        Merge(array, low, mid, high)
        return array

# my_list = [2,3,6,1,23,74,35,85,21]
# print(MergeSort(my_list, 0, len(my_list) - 1))
# print(my_list)