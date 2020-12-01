# shamelessly copied from stackoverflow resources ;P

with open('/Users/alexanderheinz/Downloads/day-1.txt', 'r') as fh:
    num_list = [int(line) for line in fh]


from itertools import combinations

# expand the pairs function so that it has 3 inputs n
def findPairs(lst, K, n):
    res = []
    for var in combinations(lst, n):
        if var[0] + var[1] + var [2] == K:
            res.append((var[0], var[1], var[2]))

    return res

def prod(val) :
    res = 1
    for ele in val:
        res *= ele
    return res

print(prod((findPairs(num_list, 2020, 3)[0])))
