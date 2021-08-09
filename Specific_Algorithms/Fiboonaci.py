#  we start our journey from the top most destination state and compute its answer by taking in count the values of states 
# that can reach the destination state, till we reach the bottom most base state.

def fib(n, stored_data):
    if n == 0 or n == 1:
        stored_data[n] = n
    if stored_data[n] is None:
        stored_data[n] = fib(n - 1, stored_data) + fib(n - 2, stored_data)
    return stored_data[n]

a_list = [None]*101
print(fib(34, a_list))