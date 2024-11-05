def ToiUuChuoi(str):
    s=str
    s=s.strip()
    a=s.split(' ')
    s=""
    for x in a:
        word=x
        if len(word.strip())!=0:
            s+=word.capitalize()+" "
    return s
str=input("nhập chuỗi: ")
print("Chuỗi sau khi tối ưu: ",ToiUuChuoi(str))