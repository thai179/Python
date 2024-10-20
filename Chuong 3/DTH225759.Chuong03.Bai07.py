from datetime import datetime, timedelta

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))


try:
    ngay_hien_tai = datetime(nam, thang, ngay)
    ngay_ke_tiep = ngay_hien_tai + timedelta(days=1)
    print("Ngày kế tiếp là:", ngay_ke_tiep.strftime("%d/%m/%Y"))
except ValueError:
    print("Ngày không hợp lệ. Vui lòng kiểm tra lại.")