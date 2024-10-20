thang=0
while thang<1 or thang >12:
    thang = int(input("Nhập tháng (1-12): "))
if thang in [1, 2, 3]:
    print(f"Tháng {thang} thuộc quý 1.")
elif thang in [4, 5, 6]:
    print(f"Tháng {thang} thuộc quý 2.")
elif thang in [7, 8, 9]:
    print(f"Tháng {thang} thuộc quý 3.")
elif thang in [10, 11, 12]:
    print(f"Tháng {thang} thuộc quý 4.")


