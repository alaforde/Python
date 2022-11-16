from itertools import permutations

s = input()
k = permutations(s)
for x in k:
    print(''.join(x))
