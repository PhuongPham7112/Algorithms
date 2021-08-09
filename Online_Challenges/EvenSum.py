# link https://www.codechef.com/DEC20B/problems/EVENPSUM
import sys
import math

def EvenSum (num1, num2):
    pairs = 0
    # even + even = even, and odd + odd = even
    # num1 is even or odd? how many numbers from 1 to num1? => determine how many odds and evens between 1 and num1
    # same for num2
    # then pairs = num1 even * num2 even and pairs = num1 odd * num2 odd
    length1 = num1
    length2 = num2
    
    if num1 % 2 != 0:
        odd_num_1 = math.ceil(length1/2)
        even_num_1 = length1 - odd_num_1
    elif num1 % 2  == 0:
        odd_num_1 = length1//2
        even_num_1 = length1//2
    
    if num2 % 2 != 0:
        odd_num_2 = math.ceil(length2/2)
        even_num_2 = length2 - odd_num_2
    elif num2 % 2  == 0:
        odd_num_2 = length2//2
        even_num_2 = length2//2

    pairs += odd_num_1*odd_num_2
    pairs += even_num_1*even_num_2

    return pairs

user_input = [line.rstrip() for line in sys.stdin.readlines()]

num1 = []
num2 = []

for i in user_input[1:]:
    a_list = i.split(' ')
    num1.append(a_list[0])
    num2.append(a_list[1])

for i in range(int(user_input[0])): # number of data tests
    print(EvenSum(int(num1[i]), int(num2[i])))