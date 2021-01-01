
# Merge two sorted sublists A[low .. mid] and A[mid + 1 .. high]
def Merge(arr, temporary_arr, low_point, mid_point, high_point):
    i = k = low_point
    j = mid_point + 1
    inversion_count = 0
    
    # Conditions are checked to make sure that  
    # i and j don't exceed their 
    # subarray limits. 
    while i <= mid_point and j <= high_point:
        if arr[i] < arr[j]:
            temporary_arr[k] = arr[i]
            i += 1
        elif arr[j] < arr[i]:
            temporary_arr[k] = arr[j]
            j += 1
            inversion_count += mid_point - i + 1
        k += 1
    
    # Copy the remaining of left and right (in the case we run out of elements in one of our copies)
    while i <= mid_point:
        temporary_arr[k] = arr[i]
        k += 1
        i += 1
    
    while j <= high_point:
        temporary_arr[k] = arr[j]
        k += 1
        j += 1

    # Copy the temporary to the original array
    for index in range(low_point, high_point + 1):
        arr[index] = temporary_arr[index]

    return inversion_count 
        


def Merge_and_count (arr, temporary_arr, low_point, high_point):
    inversion_count = 0
    if high_point > low_point:
        mid_point = (low_point + high_point) // 2
        # recursively split runs into two halves until run size == 1,
        inversion_count += Merge_and_count(arr, temporary_arr, low_point, mid_point) # split / merge left half
        inversion_count += Merge_and_count(arr, temporary_arr, mid_point + 1, high_point) # split / merge right half

        # then merge them and return back up the call chain
        inversion_count += Merge(arr, temporary_arr, low_point, mid_point, high_point) # merge the two half runs, through three variables low, high, mid
        
    return inversion_count



my_list = [1, 3, 5, 2, 4, 6, 12, 67, 19, 54, 100, 96, 7]
temp = [0] * len(my_list)
print(Merge_and_count(my_list, my_list.copy(), 0, len(my_list) - 1))