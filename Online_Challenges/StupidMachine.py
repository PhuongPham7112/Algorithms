# source: https://www.codechef.com/LRNDSA02/problems/STUPMACH
import sys
def StupidMachine():
    N = int(sys.stdin.readline())
    max_of_boxes = [int(i) for i in list(sys.stdin.readline().strip('\n'))]
    max_capacity = min(max_of_boxes)
    filled_boxes = [0]*N
    checking = True
    while checking:
        for i in range(N):
            if filled_boxes[i] < max_of_boxes[i]:
                filled_boxes[i] += max_capacity
            else:
                checking = False
                break
                
    return sum(filled_boxes)

print(StupidMachine())