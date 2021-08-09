# Question 1

# In this programming assignment you will implement one or more of the integer multiplication algorithms described in lecture.
# To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers. 
# You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement 
# recursive integer multiplication and/or Karatsuba's algorithm.

import math

def Karatsuba(num1, num2):
    if (num1 < 10) or (num2 < 10):
        return num1*num2
    else:
        size = max(len(str(num1)), len(str(num2)))
        middle = int(math.ceil(float(size) / 2))
        
        # divide number by half
        upper1 = int(math.floor(num1 / (10 ** middle)))
        lower1 = int(math.floor(num1 % (10 ** middle)))
        upper2 = int(math.floor(num2 / (10 ** middle)))
        lower2 = int(math.floor(num2 % (10 ** middle)))
        
        # Karatsuba's algorithm
        z0 = Karatsuba(lower1, lower2)
        z1 = Karatsuba((lower1 + upper1), (lower2 + upper2)) 
        z2 = Karatsuba(upper1, upper2)

        return (z2 * 10 ** (middle * 2)) + ((z1 - z2 - z0) * 10 ** middle) + z0


print(Karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))
# print(Karatsuba(1234, 6789))