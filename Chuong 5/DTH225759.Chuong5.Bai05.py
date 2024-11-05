chuoi=input("Nhập chuỗi:")
tmp=chuoi.upper()
dem=0
for i in range(len(chuoi)):
    if chuoi[i] == tmp[i] and tmp[i]!=" ":
        dem+=1
print("Số ký tự in hoa: ",dem)
tmp=chuoi.lower()
dem=0
for i in range(len(chuoi)):
    if chuoi[i] == tmp[i] and tmp[i]!=" ":
        dem+=1
print("Số ký tự in thường: ",dem)
dem=0
temp=["0","1","2","3","4","5","6","7","8","9"]
for i in range(len(chuoi)):
    if chuoi[i] in temp:
        dem+=1
print("Số lượng chữ số: ",dem)
dem=0
temp=["+","-","*","/","!","@","#","$","%","^","&","(",")","'",",","`","~","=","<",">"]
for i in range(len(chuoi)):
    if chuoi[i] in temp:
        dem+=1
print("Số lượng ký tự đặc biệt: ",dem)
dem=0
for i in range(len(chuoi)):
    if chuoi[i] == " ":
        dem+=1
print("Số lượng khoảng trắng: ",dem)
dem=0
tmp=chuoi.lower()
temp=["a","e","i","o","u","y"]
for i in range(len(chuoi)):
    if tmp[i] in temp:
        dem+=1
print("Số lượng nguyên âm: ",dem)
dem=0
temp=["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
for i in range(len(chuoi)):
    if tmp[i] in temp:
        dem+=1
print("Số lượng phụ âm: ",dem)