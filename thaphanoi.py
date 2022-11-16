def TowerOfHaNoi(n, source, target, midpoint):
    if n == 1:
        print(source, "->", target)
        return 
    TowerOfHaNoi(n-1, source, midpoint, target)
    print(source, "->", target)
    TowerOfHaNoi(n-1, midpoint, target, source)
n = int(input())
TowerOfHaNoi(n, 'A', 'C', 'B')
