def Permutation(permutation, elements, positions):
    if len(permutation) == len(elements):
        print(permutation)
    else:
        for i in range(0, len(elements)):
            if positions[i]:
                continue
            positions[i] = True
            permutation.append(elements[i])
            Permutation(permutation, elements, positions)
            permutation.remove(elements[i])
            positions[i] = False

Permutation([], [1, 2, 3, 4], [False]*len([1, 2, 3, 4]))
