import collections


t = int(input())
l = []
for i in range(t):
    s = input().lower()
    s = s.replace('.', ' ')
    s = s.replace('!', ' ')
    s = s.replace('?', ' ')
    s = s.replace('/', ' ')
    s = s.replace('-', ' ')
    s = s.strip().split()
    for i in range(len(s)):
        if s[i].isalpha():
            l.append(s[i])
c = collections.Counter(l)
print(c)
    
    