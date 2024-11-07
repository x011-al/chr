import requests
from time import time

def load_proxies_from_file(filename):
    # Membaca daftar proxy dari file
    try:
        with open(filename, 'r') as file:
            proxies = file.read().splitlines()
        return proxies
    except FileNotFoundError:
        print(f"File '{filename}' tidak ditemukan.")
        return []

def save_active_proxy(proxy, latency):
    # Menyimpan proxy aktif ke file 'local_proxies.txt' dengan prefix 'http://'
    if not proxy.startswith("http://") and not proxy.startswith("https://"):
        proxy = "http://" + proxy  # Menambahkan 'http://' jika belum ada
    with open("local_proxies.txt", "a") as file:
        file.write(f"{proxy} - Latency: {latency:.2f} seconds\n")

def check_proxy(proxy):
    url = "http://httpbin.org/ip"  # Situs uji untuk melihat alamat IP
    proxies = {
        "http": proxy,
        "https": proxy,
    }
    try:
        start_time = time()  # Mulai waktu
        response = requests.get(url, proxies=proxies, timeout=5)  # Batas waktu 5 detik
        latency = time() - start_time  # Hitung latensi
        if response.status_code == 200:
            print(f"Proxy {proxy} aktif.")
            print(f"Latensi: {latency:.2f} detik")
            print(f"IP yang terdeteksi: {response.json()['origin']}")
            save_active_proxy(proxy, latency)  # Simpan proxy aktif ke file
            return True, latency
        else:
            print(f"Proxy {proxy} tidak aktif (Kode status: {response.status_code}).")
            return False, None
    except requests.RequestException as e:
        print(f"Proxy {proxy} tidak aktif (Error: {e}).")
        return False, None

# Memuat proxy dari file
proxy_list = load_proxies_from_file("proxies.txt")

# Hapus isi 'local_proxies.txt' jika sudah ada untuk menyimpan hasil baru
open("local_proxies.txt", "w").close()

# Uji setiap proxy dari file
for proxy in proxy_list:
    status, latency = check_proxy(proxy)
    print("-" * 50)
