class agent:
    def __init__(self, name, score):
        self.name = name
        self.score = score

agents = []
for _ in range(5):
    name, score = input().split()
    agents.append(agent(name, int(score)))

agents.sort(key = lambda x : x.score)
print(agents[0].name, agents[0].score)