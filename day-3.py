# open as list
with open('/Users/alexanderheinz/Downloads/day-3.txt', 'r') as fh:
    num_list = [str(line) for line in fh]

del num_list[0]

loopcount = 0
counter = 0
for i in num_list:
    loopcount += 3

    if loopcount > 30:
        loopcount = loopcount % 31

    if i[loopcount] == "#":
        counter += 1


print(counter)


# part 2:
loopcount = 0
counter_2 = 0
for i in num_list:
    loopcount += 1

    if loopcount > 30:
        loopcount = loopcount % 31

    if i[loopcount] == "#":
        counter_2 += 1

print(counter_2)
loopcount = 0
counter_3 = 0
for i in num_list:
    loopcount += 5

    if loopcount > 30:
        loopcount = loopcount % 31

    if i[loopcount] == "#":
        counter_3 += 1

print(counter_3)

loopcount = 0
counter_4 = 0
for i in num_list:
    loopcount += 7

    if loopcount > 30:
        loopcount = loopcount % 31

    if i[loopcount] == "#":
        counter_4 += 1
print(counter_4)


del(num_list[0])

loopcount = 0
counter_5 = 0
for i in num_list[::2]:

    loopcount += 1

    if loopcount > 30:
        loopcount = loopcount % 31

    if i[loopcount] == "#":
        counter_5 += 1

print(counter_5)

print(counter*counter_2*counter_3*counter_4*counter_5)
