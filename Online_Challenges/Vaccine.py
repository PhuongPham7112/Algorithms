# Finally, a COVID vaccine is out on the market 
# and the Chefland government has asked you to form a plan to distribute it to the public as soon as possible. 
# There are a total of N people with ages a1,a2,…,aN
# There is only one hospital where vaccination is done and it is only possible to vaccinate up to D people per day. 
# Anyone whose age is ≥80 or ≤9 is considered to be at risk. 
# On each day, you may not vaccinate both a person who is at risk and a person who is not at risk. 
# Find the smallest number of days needed to vaccinate everyone.
# The first line of each test case contains two space-separated integers N and D.
# The second line contains N space-separated integers a1,a2,…,aN.
# link https://www.codechef.com/DEC20B/problems/VACCINE2

import sys
import math

def Vaccine2 (people_number, test_cases, people_age):
    days = 0

    # convert every data to integer type
    people_number = int(people_number)
    test_cases = int(test_cases)
    int_people_age = map(lambda x: int(x), people_age)

    # if test case is 1, there's no need for grouping
    if test_cases == 1:
        days = people_number
        return days
    elif test_cases > 1:

        at_risk_people = []
        normal_people = []

        for i in int_people_age:
            if i <= 9 or i >= 80:
                at_risk_people.append(i)
            elif 9 < i < 80:
                normal_people.append(i)
        
        days += (math.ceil(len(normal_people)/test_cases))
        days += (math.ceil(len(at_risk_people)/test_cases))

        return days
        

# read input
user_input = [line.rstrip() for line in sys.stdin.readlines()]
people_number = []
test_cases = []
people_age = []
for i in user_input[1:]:
    if user_input.index(i) % 2 != 0: 
        a_list = i.split(' ')
        people_number.append(a_list[0])
        test_cases.append(a_list[1])
    elif user_input.index(i) % 2 == 0:
        a_list = i.split(' ')
        people_age.append(a_list)

i = 0
while i < int(user_input[0]): # number of data tests
    print(Vaccine2(people_number[i], test_cases[i], people_age[i]))
    i += 1