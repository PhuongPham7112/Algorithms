# link: https://community.topcoder.com/stat?c=problem_statement&pm=10860
# resources: https://www.journaldev.com/43675/subset-sum-problem-dynamic-programming-java
def LotteryTicket(price, b1, b2, b3, b4):
    checks = [b1, b2, b3, b4]
    n = len(checks)
    boolean_array = ([[False for i in range(price + 1)] for i in range(n + 1)])
    for i in range(n + 1):
        boolean_array[i][0] = True

    for i in range(1, price + 1):
        boolean_array[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, price + 1):
            if checks[i - 1] > j:
                boolean_array[i][j] = boolean_array[i - 1][j]
            elif checks[i - 1] <= j:
                boolean_array[i][j] = boolean_array[i - 1][j] or boolean_array[i - 1][j - checks[i - 1]]
    return boolean_array[n][price], boolean_array

print(LotteryTicket(65,1,5,10,50))
# A Dynamic Programming solution for subset 
# sum problem Returns true if there is a subset of 
# set[] with sun equal to given sum 

# Returns true if there is a subset of set[] 
# with sun equal to given sum
# def isSubsetSum(set, n, sum):
    
# 	# The value of subset[i][j] will be 
# 	# true if there is a
# 	# subset of set[0..j-1] with sum equal to i
# 	subset =([[False for i in range(sum + 1)] 
# 		for i in range(n + 1)])
    
# 	# If sum is 0, then answer is true 
# 	for i in range(n + 1):
# 		subset[i][0] = True
        
# 	# If sum is not 0 and set is empty, 
# 	# then answer is false 
# 	for i in range(1, sum + 1):
# 		subset[0][i]= False

# 	# Fill the subset table in botton up manner
# 	for i in range(1, n + 1):
# 		for j in range(1, sum + 1):
# 			if j<set[i-1]:
# 				subset[i][j] = subset[i-1][j]
# 			if j>= set[i-1]:
# 				subset[i][j] = (subset[i-1][j] or
# 								subset[i - 1][j-set[i-1]])

# 	# # uncomment this code to print table 
#     # for i in range(n + 1):
#     #     for j in range(sum + 1):
#     #         print (subset[i][j], end =" ")
#     #         print()
# 	return subset[n][sum]
        
# # Driver code
# if __name__=='__main__':
# 	set = [3, 34, 4, 12, 5, 2]
# 	sum = 9
# 	n = len(set)
# 	if (isSubsetSum(set, n, sum) == True):
# 		print("Found a subset with given sum")
# 	else:
# 		print("No subset with given sum")
        
# This code is contributed by 
# sahil shelangia. 
