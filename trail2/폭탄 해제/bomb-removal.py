class pwd:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

code, color, second = input().split()
pwd1 = pwd(code, color, int(second))
print("code :", pwd1.code)
print("color :", pwd1.color)
print("second :", pwd1.second)