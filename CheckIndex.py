def CheckIndex(arr):
    for i in arr:
        if i == arr[i]:
            return True
        elif i != arr[i]:
            continue

test_list = [-1, 1, 2, 3, 5, 6]
print(CheckIndex(test_list))
