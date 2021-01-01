# You are a given a unimodal array of n distinct elements, meaning that its entries are in increasing order up until its maximum element, 
# after which its elements are in decreasing order. 
# Give an algorithm to compute the maximum element that runs in O(log n) time.
# if the last element of left is smaller than first element of right, search right. If else, search left. Repeat
def Search(arr):
    low = 0
    high = len(arr) - 1
    if len(arr) == 1:
        print(arr[low])
    elif len(arr) > 1:
        mid = (low + high) // 2
        left = arr[:mid + 1]
        right = arr[mid + 1:]
        if left[-1] < right[0]:
            Search(right)
        elif left[-1] > right[0]:
            Search(left)

test_list = [1, 3, 6, 7, 5, 3, 2, 1]
Search(test_list)