n = int(input()) 
str = input() 
l = list(map(int, str.split(" ")))
b = 1 
while b: 
    b = 0 
    i = 0 
    while(i < len(l)-1): 
        if (l[i]^l[i + 1]) % 2 == 0: 
            del l[i] 
            del l[i] 
            b = 1 
        i += 1 
print(len(l))