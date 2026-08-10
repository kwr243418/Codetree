class user:
    def __init__(self, id = 'codetree', lv = 10):
        self.id = id
        self.lv = lv

user1 = user()
print(f"user {user1.id} lv {user1.lv}")
id, lv = input().split()
lv = int(lv)
user1 = user(id, lv)
print(f"user {user1.id} lv {user1.lv}")