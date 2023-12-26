# Import necessary modules
import requests
import threading
import time

# Mendefinisikan fungsi untuk mendownload file
# I.S. File belum terdownload di penyimpanan lokal
# F.S. File telah didownload di penyimpanan lokal
# dengan bantuan metode get() dari modul requests,
# bersumber dari URL nilai dari string url 
# dan nama file adalah nilai dari string filename
def download_file(url, filename):
    # Melakukan request HTTP GET kepada URL yang 
    # diberikan sebagai parameter
    r = requests.get(url, allow_redirects=True)
    # Mengecek kode respons. Jika kodenya 200 maka
    # program akan menulis file hasil download
    # dari konten HTTP response tersebut, dengan 
    # nama file filename. Jika sebaliknya maka muncul
    # pesan error
    if r.status_code==200:
        open(filename, 'wb').write(r.content) # Write binary, karena r.content dalam bentuk byte
        print('File', filename, 'berhasil didownload dari', url)
    else:
        print("Failed to download", filename, "from", url, "Error", r.status_code)

# Kelas Downloader sebagai kelas worker, 
# merupakan inheritance dari kelas Thread dari
# modul threading
class Downloader(threading.Thread):
    # Konstruktor untuk instansiasi obyek
    # Memiliki dua atribut yaitu url dan filename
    # Satu obyek instansiasi kelas ini mewakili
    # pengunduhan satu file dari sumber URL 
    # nilai dari string url, dengan nama file
    # berupa nilai dari string filename
    def __init__(self, url, filename):
        threading.Thread.__init__(self)
        self.url = url
        self.filename = filename 

    # Fungsi yang dijalankan saat memanggil metode start() 
    def run(self):
        download_file(self.url, self.filename)

# Main function
if __name__ == '__main__':
    # Sambutan
    print("||+==========+|| Selamat datang di Program Parallel Downloader ||+=========+||")
    print("\nCreated by: \nKaisar Kertarajasa"+"\nSatya Rayyis Baruna"+"\nNadim Rafli Hamzah"+"\nEzra Obadiah Wowor")
    
    # Endless loop 
    while True:
        # Program meminta konfirmasi pengguna apakah ingin memulai program
        start_program = input("Apa anda ingin memulai program? (ya/tidak): ")
        
        # Jika pengguna mengetik 'ya' maka program akan melakukan fungsionalitas utamanya
        if start_program.lower() == 'ya':
            # Meminta masukan dari user berapa banyak file yang ingin diunduh
            num_files = int(input("Masukkan berapa banyak file yang ingin didownload: "))

            # Daftar untuk menyimpan thread
            threads = []

            # Looping sebanyak berapa file yang ingin diunduh pengguna
            for i in range(1, num_files + 1):
                # Meminta input URL sumber file
                url = input(f"\nMasukkan URL file {i}: ")
                # Meminta input nama file hasil download untuk disimpan secara lokal
                filename = input(f"Masukkan nama untuk file {i}: ")

                #thread = threading.Thread(target=download_file, args=(url, filename))

                # Instansiasi kelas Downloader lalu disimpan pada list threads
                thread = Downloader(url, filename)
                threads.append(thread)
            
            # Mencatat waktu dimulainya pengunduhan
            start = time.time()

            # Menjalankan setiap thread
            for thread in threads:
                thread.start()

            # Mengakhiri thread
            for thread in threads:
                thread.join()
            
            # Mencatat waktu selesainya pengunduhan
            end = time.time()

            # Melaporkan durasi waktu
            print("Elapsed time:", end-start, "seconds")

        # Apabila pengguna tidak ingin melanjutkan program
        else:
            print("Karena Anda bermaksud tidak memulai program, maka program otomatis akan keluar.")
            time.sleep(3)
            quit()
