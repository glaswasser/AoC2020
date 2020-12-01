# shamelessly copied from stackoverflow resources ;P

# this is the first part

with open('/Users/alexanderheinz/Downloads/day-1.txt', 'r') as fh:
    num_list = [int(line) for line in fh]
print(num_list.pop())

# function to find pairs that equal a value K
def findPairs(lst, K):
    res = []
    while lst:
        num = lst.pop()
        diff = K - num
        if diff in lst:
            res.append((diff, num))

    res.reverse()
    return res



# Driver code
K = 2020
#print(findPairs(num_list, K))

# function to multiply tuples
def prod(val) :
    res = 1
    for ele in val:
        res *= ele
    return res
#print result
print(prod(list(findPairs(num_list, K)[0])))
