def ktDoiXung(s):
    for i in range(len(s)):
        if s[i]!=s[len(s)-i-1]:
            return False
    return True

while True:
    chuoi=input("Nhập chuỗi cần kiểm tra đối xứng: ")
    if(ktDoiXung(chuoi)):
        print("Chuỗi",chuoi,"đối xứng")
    else:
        print("Chuỗi",chuoi,"không đối xứng")
    tmp=input("Bạn có muốn tiếp tục không (c/k): ")
    if tmp == "k":
        break