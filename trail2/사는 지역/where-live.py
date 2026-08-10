class people:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city


n = int(input())
pp = []
for _ in range(n):
    name, addr, city = input().split()
    pp.append(people(name, addr, city))

pp.sort(key = lambda x : x.name, reverse = True)

print("name", pp[0].name)
print("addr", pp[0].addr)
print("city", pp[0].city)