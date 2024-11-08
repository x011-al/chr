import pyautogui
import time
import sys
from datetime import datetime, timedelta

# Setel fail-safe menjadi False
pyautogui.FAILSAFE = False

# Koordinat untuk klik
coordinates_1 = (173, 290)  # Koordinat pertama
coordinates_2 = (179, 284)  # Koordinat kedua

# Durasi program berjalan (24 jam)
end_time = datetime.now() + timedelta(hours=24)

# Loop klik
while datetime.now() < end_time:
    # Melakukan double-click di koordinat pertama
    pyautogui.moveTo(coordinates_1[0], coordinates_1[1], duration=0.5)
    pyautogui.doubleClick()
    time.sleep(1)  # Menunggu 1 detik sebelum pindah ke koordinat berikutnya
    
    # Melakukan double-click di koordinat kedua
    pyautogui.moveTo(coordinates_2[0], coordinates_2[1], duration=0.5)
    pyautogui.doubleClick()
    time.sleep(15)  # Tunggu 5 detik sebelum mengulangi proses

print("24 jam telah selesai. Program berakhir.")
sys.exit()
