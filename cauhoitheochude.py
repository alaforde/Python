t = int(input())
s = [None]*(t+5)
s[0] = ""
s[t+1] = ""
for i in range(1, t+1):
    s[i] = input()
pre = 0
print(s[1], end = ': ')
for i in range(2,t+2):
    if s[i] == "" and i != t+1:
        print(i-pre-2)
        pre = i
        print(s[i+1], end = ': ')
print(t+1 - pre-2)

        
        