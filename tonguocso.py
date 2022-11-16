import math

t = int(input())
a = [0]*1000001
for i in range(1000001):
    a[i] = i
for i in range(2,(int)(math.sqrt(1000001))):    
    for j in range(i*i,1000001, i):
        if(a[j] == j):
            a[j] = i
for i in range(1000001):
    print(a[i])
    