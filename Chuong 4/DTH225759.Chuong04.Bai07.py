from math import sqrt
def TinhDoDai(xa, ya, xb, yb):
    return sqrt((xb-xa)**2 + (yb-ya)**2)
xa=int(input("Nhập vào giá trị của xa: "))
ya=int(input("Nhập vào giá trị của ya: "))
xb=int(input("Nhập vào giá trị của xb: "))
yb=int(input("Nhập vào giá trị của yb: "))
print("Khoảng cách giữa 2 điểm A B là: ", TinhDoDai(xa,ya,xb,yb))