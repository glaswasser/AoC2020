import re

# open as list
with open('/Users/alexanderheinz/Downloads/day-2.txt', 'r') as fh:
    num_list = [str(line) for line in fh]


# part 1:
counter = 0
for i in num_list:
    # what to look for
    to_look = re.search("[a-z]", i)
    # get the range of digits
    range_1 = re.search("\d+", i).group()
    range_2 = re.search("-\d+", i).group()[1:]

    # get the count of desired letters
    letter_counter = i.count(to_look.group())-1

    # count +1 if it's valid
    if int(range_1) <= int(letter_counter) <= int(range_2):
        counter += 1

print(counter)


# part 2:
counter = 0
for i in num_list:
    # the range
    range_1 = int(re.search("\d+", i).group())
    range_2 = int(re.search("-\d+", i).group()[1:])
    # what to look for
    to_look = re.search("[a-z]", i).group()
    # what to check
    to_check = i.partition(":")[2]

    # if the sum of both booleans is one (one true), add one to the counter
    if int(to_look == to_check[range_1]) + int(to_look == to_check[range_2]) == 1:
        counter +=1

print(counter)
