# link: https://www.hackerrank.com/challenges/the-power-sum/problem
# resources: https://www.geeksforgeeks.org/coin-change-dp-7/ and https://www.hackerrank.com/challenges/the-power-sum/editorial
def count_expressions(number, power, sumSoFar, currentValue):
    
    if sumSoFar == number:
        return 1
    else:
        print(sumSoFar, currentValue)
        print("add first 1")
        currentValue += 1
        answer = 0
        while sumSoFar + currentValue**power <= number:
            print("not there yet, recurse")
            answer += count_expressions(number, power, sumSoFar + currentValue**power, currentValue)
            print("add another 1 and go back to the start of the while loop")
            currentValue += 1
        else:
            print("too big", sumSoFar, currentValue)
        return answer

print(count_expressions(29, 2, 0, 0))