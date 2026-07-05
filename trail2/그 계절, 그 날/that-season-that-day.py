Y, M, D = map(int, input().split())

# Please write your code here.
def season(Y, M, D):
    md1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    md2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    yoonyear = False
    if Y % 4 == 0:
        yoonyear = True
        if Y % 100 == 0:
            yoonyear = False
            if Y % 400 == 0:
                yoonyear = True
    if not 1 <= M <= 12:
        print('-1')
    if yoonyear:
        if 1 <= D <= md2[M-1]:
            if 3 <= M <= 5:
                print("Spring")
            elif 6 <= M <= 8:
                print("Summer")
            elif 9 <= M <= 11:
                print("Fall")
            else:
                print("Winter")
        else:
            print('-1')
    else:
        if 1 <= D <= md1[M-1]:
            if 3 <= M <= 5:
                print("Spring")
            elif 6 <= M <= 8:
                print("Summer")
            elif 9 <= M <= 11:
                print("Fall")
            else:
                print("Winter")
        else:
            print('-1')


season(Y, M, D)