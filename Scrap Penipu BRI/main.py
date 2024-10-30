# Sebelum menjalankan skrip ini, perhatikan langkah berikut
# Jalankan pada terminal atau cmd "pip install selenium Faker"

import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select

# Mendefinisikan faker
fake = Faker('id_ID')

def generate_nohp():
    return "08" + fake.random_element(["1", "2", "3", "5", "7", "9"]) + str(fake.random_number(9))

# URL Target
url_target = "https://choreoapps.kf-dflow.cfd/dr/"

# Konfigurasi chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")

# Inisialisasi web driver
driver = webdriver.Chrome(chrome_options)
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)

for count in range(250):

    # Memulai aksi kerjain penipu
    driver.get(url_target)

    # ----- 1. Halaman Pertama
    # Mendapatkan elemen select dan pilih opsi
    select_tarif = driver.find_element(By.NAME, "tarif")
    tarif = Select(select_tarif)
    tarif.select_by_index(2)

    # Mendapatkan elemen input no hp dan isi
    no_hp = driver.find_element(By.NAME, "nohp")
    no_hp.send_keys(generate_nohp())

    time.sleep(2)

    # Mendapatkan tombol lanjutkan
    lanjutkan = driver.find_element(By.ID, "kirim")
    lanjutkan.click()

    # ----- 2. Halaman Kedua
    # Mendapatkan element input nama ktp dan isi
    nama_ktp = driver.find_element(By.NAME, "nama")
    nama_ktp.send_keys(fake.name())

    # Mendapatkan element nomor rekening dan isi
    no_rekening = driver.find_element(By.NAME, "rek")
    no_rekening.send_keys(fake.random_number(15))

    time.sleep(2)

    # Mendapatkan tombol lanjutkan
    lanjutkan = driver.find_element(By.ID, "kirim")
    lanjutkan.click()

    # Mendapatkan element input saldo
    saldo = driver.find_element(By.NAME, "saldo")
    saldo.send_keys(fake.random_number(8))

    time.sleep(1)

    # Mendapatkan tombol lanjutkan
    lanjutkan = driver.find_element(By.ID, "kirim")
    lanjutkan.click()

    for i in range(10):
        # Mendapatkan element input OTP
        otp = driver.find_element(By.NAME, "otp")
        otp.send_keys(fake.random_number(6))
        otp.send_keys(Keys.RETURN)

        # Mendapatkan tombol lanjutkan
        # lanjutkan = driver.find_element(By.ID, "kirims")
        # lanjutkan.click()

        time.sleep(3)
    
    print(f"Berhasil percobaan ke - {count + 1}")

# Keluar dari driver
driver.quit()