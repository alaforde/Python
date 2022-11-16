import math
from tabnanny import check
t = int(input())
for i in range(t):
    s1 = input()
    s2 = s1[::-1]
    check = 0
    for j in range(1, len(s1)//2 + 1):
        if abs(ord(s1[j])- ord(s1[j-1])) != abs(ord(s2[j])- ord(s2[j-1])):
            check = 1
    if(check):
        print("NO")
    else:
        print("YES")