# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]


import itertools
def limitedPowerSet(n, k):
    # Your code goes here...
    # pass
    li = [{}]
    s = set()
    for i in range(n):
        s.add(i+1)
    for i in range(len(s)):
        x = list(map(set, itertools.combinations(s,i+1)))
        for j in range(len(x)):
            if len(li) != k:
                li.append(x[j])
            else:
                return li
 
assert(limitedPowerSet(5, 7) == [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ])
print("\nAll test cases passed...!")
