
with open('/Users/alexanderheinz/Downloads/day-9.txt', 'r') as fh:
    num_list = [int(line) for line in fh]

from itertools import combinations

result = []
for i in range(25,len(num_list)):
    #print(num_list)
    #i = 25
    target = num_list[i]
    #print("target", target)
    prev = num_list[i-25:i]
    #print(prev)
    comb = combinations(prev, 2)

    sums = [sum(i) for i in comb]
    #print("sums", sums)
    if target not in sums:
        result.append(target)
    #print(target in sums)
print(result)
#comb = [combinations(prev, 2) for i in prev]
#print(comb)
