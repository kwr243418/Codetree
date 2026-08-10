class product:
    def __init__(self, name = 'codetree', code = 50):
        self.name = name
        self.code = code

pd = product()
print(f"product {pd.code} is {pd.name}")
name, code = input().split()
pd = product(name, int(code))
print(f"product {pd.code} is {pd.name}")