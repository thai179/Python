n=int(input("Nhập số phần tử: "))
lst=[]
for i in range(n):
    tmp=float(input(f"nhập số thứ[{i}]:"))
    lst.append(tmp)
print("List ngẫu nhiên là:")
print(lst)
lst.sort()
print("list sau khi sắp xếp:",lst)