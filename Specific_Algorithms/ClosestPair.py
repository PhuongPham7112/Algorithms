from math import sqrt

Pairs = [[2, 3], [12, 30], [40, 50], [12, 10], [3, 4], [5, 1], [7, 6], [0, 0], [8, 7], [0, 1]]
Pairs.sort(key = lambda x: x[0])

def Distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def ClosestSplitPair(P, S, mid):
    mid_bar_x = P[mid][0]
    lowest_x = mid_bar_x - S
    highest_x = mid_bar_x + S
    Sy = [i for i in P if lowest_x <= i[0] <= highest_x]
    Sy.sort(key = lambda x: x[1])

    min_dist = S
    best_pair = [0, 0]
    for i in range(0, len(Sy) - 1):
        for j in range(i + 1, min(7, len(Sy) - i)):
            point1 = Sy[i]
            point2 = Sy[i + j]
            if Distance(point1, point2) < min_dist:
                best_pair = [point1, point2]
                min_dist = Distance(point1, point2)
    
    return min_dist 

def ClosestPair(P):
    low = 0
    high = len(P) - 1
    if len(P) > 3:
        mid = (high + low)//2
        Pleft = P[:mid + 1]
        Pright = P[mid + 1:]
        closest_left = ClosestPair(Pleft)
        closest_right = ClosestPair(Pright)
        S = min(closest_left, closest_right)
        return S
    elif len(P) == 3:
        return min(Distance(P[0], P[1]), Distance(P[1], P[2]), Distance(P[0], P[2]))
    elif len(P) == 2:
        return Distance(P[0], P[1])
    

print(Pairs)
print(ClosestPair(Pairs))
print(ClosestSplitPair(Pairs, ClosestPair(Pairs), (0 + len(Pairs))//2))