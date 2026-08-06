secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class smt:
    def __init__(self, s, m, t):
        self.s = s
        self.m = m
        self.t = t

smt1 = smt(secret_code, meeting_point, time)
print(f"secret code : {smt1.s}")
print(f"meeting point : {smt1.m}")
print(f"time : {smt1.t}")