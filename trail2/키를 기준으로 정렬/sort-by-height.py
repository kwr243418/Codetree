class prd:
    def __init__(self, name, height, kg):
        self.name = name
        self.height = height
        self.kg = kg

n = int(input())
prdl = []
for _ in range(n):
    name, height, kg = input().split()
    prdl.append(prd(name, int(height), int(kg)))

prdl.sort(key = lambda x : x.height)
for i in prdl:
    print(i.name, i.height, i.kg)