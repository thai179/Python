import math
try:
    r=float(input("nhập vào bán kính đường tròn: "))
    cv=2*math.pi*r
    dt=math.pi*r*r
    print("chu vi = ",cv)
    print("diện tích =",dt)
except:
    print("lỗi rồi!!!")
    