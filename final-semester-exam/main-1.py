import numpy as np
import matplotlib.pyplot as plt

# Thông số tín hiệu
T = 20  # Độ dài tín hiệu (giây)
Fs = 250  # Tần suất lấy mẫu (số mẫu/giây)
f1 = 8  # (Hz)
f2 = 30  # (Hz)

# Tạo dữ liệu vẽ đồ thị tín hiệu
Ts = 1 / Fs
t = np.arange(0, T, Ts)  # Vector thời gian từ 0 đến T với bước nhảy Ts
x = np.sin(2 * np.pi * f1 * t)
y = np.sin(2 * np.pi * f2 * t)
z = x + y

# Hiển thị đồ thị tín hiệu
plt.figure(figsize=(10, 4))
plt.plot(t, z, label='z = x + y', color='b')
plt.xlabel('Thời gian (s)')
plt.ylabel('Biên độ')
plt.title('Tín hiệu z = x + y trong miền thời gian')
plt.legend()
plt.xlim(0, 1)  # Hiển thị chỉ 1 giây đầu tiên để dễ quan sát
plt.grid()
plt.show()

# Biến đổi Fourier nhanh (FFT)
N = len(z)  # Số mẫu
Z_fft = np.fft.fft(z)  # Biến đổi Fourier
freqs = np.fft.fftfreq(N, d=1/Fs)  # Tính tần số tương ứng
Z_fft_magnitude = np.abs(Z_fft) / N  # Lấy biên độ và chuẩn hóa

# Chỉ lấy nửa phổ do tín hiệu thực
half_N = N // 2
plt.figure(figsize=(10, 4))
plt.plot(freqs[:half_N], Z_fft_magnitude[:half_N] * 2)  # Nhân 2 để bảo toàn biên độ
plt.xlabel("Tần số (Hz)")
plt.ylabel("Biên độ")
plt.title("Phổ của z")
plt.grid()
plt.show()
