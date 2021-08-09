def Permutation(permutation, elements, positions):
    if len(permutation) == len(elements):
        print(permutation)
    else:
        for i in range(0, len(elements)):
            print("this is " + str(elements[i]))
            if positions[i]:
                print("skip " + str(elements[i]))
                continue
            positions[i] = True
            print("add " + str(elements[i]))
            permutation.append(elements[i])
            print("recursion")
            Permutation(permutation, elements, positions)
            print("remove " + str(elements[i]))
            permutation.remove(elements[i])
            print("set false")
            positions[i] = False

Permutation([], [1, 2, 3, 4], [False]*len([1, 2, 3, 4]))
