class Subject:
    def __init__(self, id, name, details):
        self.id = id
        self.name = name
        self.details = details

n = int(input())
a = [None]*n
for i in range(n):
    id = input()
    name = input()
    details = input()
    a[i] = Subject(id, name, details)
a.sort(key = lambda x:x.id)
for i in range(n):
    print(a[i].id, a[i].name, a[i].details)
