a=int(input("Nhập a: "))
b=int(input("Nhập b: "))
phep=input("Nhập phép toán: ")
if phep == "+":
    tmp=a+b
    print(a,"+",b,"=",tmp)
elif phep =="-":
    tmp=a-b
    print(a,"-",b,"=",tmp)
elif phep =="*":
    tmp=a*b
    print(a,"*",b,"=",tmp)
elif phep =="*":
    tmp=a/b
    print(a,"/",b,"=",tmp)
else:
    print("Phép toán không hợp lệ!!!")