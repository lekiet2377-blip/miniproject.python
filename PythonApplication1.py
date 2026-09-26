#Bài 1
#TODO 1
#tuoi = int(input("Nhập tuổi: "))
#if tuoi <13:
    #print("Thiếu nhi")
#elif tuoi >=13 and tuoi <=17:
    #print("Thiếu niên")
#elif tuoi >=18 and tuoi <=64:
    #print("Người lớn")
#else:
    #print("Người cao tuổi")
#TODO 2
#diem = float(input("Nhập điểm: "))
#if diem >= 9:
    #print("Xuất sắc")
#elif diem >=8:
    #print("Giỏi")
#elif diem >=6.5:
    #print("Khá")
#elif diem >=5:
    #print("Trung bình")
#else:
    #print("Yếu")
#TODO 3
#nam = int(input("Nhập năm: "))
#if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 !=0):
    #print("Năm nhuận")
#else:
    #print("Không nhuận")
#TODO 4
#so1 = int(input("Nhập số 1: "))
#so2 = int(input("Nhập số 2: "))
#so3 = int(input("Nhập số 3: "))
#if so1>so2 and so1>so3:
    #print(f"Số lớn nhất là: {so1}")
#elif so2>so1 and so2>so3:
    #print(f"Số lớn nhất là: {so2}")
#else:
    #print(f"Số lớn nhất là: {so3}")
#Bài 2
#TODO 1
#tuoi = int(input("Nhập tuổi: "))
#banglai = input("Có bằng lái không(Y/N): ")
#khongsay = input("Có tỉnh táo không(Y/N): ")
#if tuoi >= 18 and (banglai.lower()== "y" and khongsay.lower() == "y"):
    #print("Đủ điều kiện lái xe")
#else:
    #print("Không đủ điều kiện lái xe")
#TODO 2
#a = float(input("Nhập cạnh a: "))
#b = float(input("Nhập cạnh b: "))
#c = float(input("Nhập cạnh c: "))
#if a + b > c and a + c >b and b + c > a:
    #print("Tạo thành tam giác")
#else:
    #print("Không tạo thành tam giác")
    #exit()
#if a==b==c:
    #print("Tam giác đều")
#elif a == b or b == c or a == c:
    #print("Tam giác cân")
#else:
    #print("Tam giác thường")
#TODO 3
#mk =  input("Nhập mật khẩu: ")
#if (len(mk)>=8 and any(n.isupper() for n in mk) and any(n.islower() for n in mk) and any(n.isdigit() for n in mk)):
    #print("Mật khẩu mạnh")
#else:
    #print("Mật khẩu yếu")
#TODO 4
#n = int(input("Nhập số: "))
#if n % 3 == 0 and n % 5 == 0:
    #print("FizzBuzz")
#elif n % 3 == 0:
    #print("Fizz")
#elif n % 5 == 0:
    #print("Buzz")
#else:
    #print(f"{n}")
#Bai 3
#TODO 1
#sodu = int(input("Nhập số dư: "))
#rut = int(input("Nhập số tiền muốn rút: "))
#if rut > 0 and sodu >= rut and rut % 50000 == 0:
    #print("Rút thành công")
#else:
    #print("Rút không thành công")
#TODO 2
#chieucao = float(input("Nhập chiều cao: "))
#cannang = int(input("Nhập cân nặng: "))
#BMI = cannang / (chieucao**2)
#if BMI < 18.5:
    #print("Thiếu cân")
#elif BMI >=18.5 and BMI <=24.9:
    #print("Cân đối")
#elif BMI >= 25 and BMI <=29.9:
    #print("Thừa cân")
#else:
    #print("Béo phì")
#TODO 3
ve = input("Loại vé (thuong/vip): ")
ngay = input("ngày (thuong/cuoi_tuan): ")
tuoi = int(input("Nhập tuổi: "))
if ve.lower() == "thuong":
    gia = 80000
elif ve.lower() == "vip":
    gia = 120000
if ngay.lower() == "cuoi_tuan":
    gia *= 1.3
if tuoi < 12 and tuoi >=65:
    gia *= 0.5
elif tuoi >= 18 and tuoi <= 25:
    gia *= 0.2
print(f"Giá vé là: ",int({gia}))






