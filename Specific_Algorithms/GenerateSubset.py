def GenerateSubset(R):
    if R == N:
        print("[ "+' '.join ( map (str,subset) ) + " ]")
    else:
        subset.append(R)
        GenerateSubset(R + 1)

        subset.pop()
        GenerateSubset(R + 1)

N = 4
subset = []
GenerateSubset(1)
