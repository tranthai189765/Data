import matplotlib.pyplot as plt

# Dữ liệu
x = [200, 220, 240, 260, 280, 300, 320, 340, 360, 380]
y1 = [0.530667, 0.550667, 0.619333, 0.648667, 0.676, 0.720667, 0.744667, 0.798667, 0.857333, 0.93]
y2 = [0.428667, 0.484667, 0.52, 0.570667, 0.622, 0.746667, 0.753333, 0.833333, 0.865333, 0.936667]
y3 = [0.517333, 0.541333, 0.606667, 0.61, 0.675333, 0.726, 0.736667, 0.826, 0.815333, 0.900667]
y4 = [0.618667, 0.654, 0.732667, 0.737333, 0.784667, 0.834, 0.842, 0.914667, 0.920667, 0.962667]

# Vẽ dữ liệu
plt.plot(x, y1, label='Memetic', marker='o')
plt.plot(x, y2, label='Prim', marker='s')
plt.plot(x, y3, label='Greedy', marker='^')
plt.plot(x, y4, label='SASB', marker='d')

# Thêm tiêu đề và nhãn trục
plt.title('Scenario 1')
plt.xlabel('NUMBER OF SENSORS')
plt.ylabel('SCORE')

# Thêm lưới
plt.grid(True)

# Đặt các giá trị trục x chỉ là số nguyên trong khoảng 200 đến 380
plt.xticks(range(200, 381, 20))  # Điều chỉnh để có các giá trị từ 200 đến 400 với bước nhảy 20

# Hiển thị chú thích
plt.legend()

# Hiển thị đồ thị
plt.show()
