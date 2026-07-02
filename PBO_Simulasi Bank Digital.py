import random
import time

class AkunBank:
    def __init__(self, nama, saldo_awal=0):
        self.nama = nama
        self.nomor_akun = random.randint(10000, 99999)
        self.saldo = saldo_awal
        self.riwayat = []  # Tambahan cek list riwayat transaksi

        if saldo_awal > 0:
            self.riwayat.append(f"Deposit Awal: +Rp{saldo_awal}") # Tambahan merekam deposit awal ke dalam riwayat

        print("\n===== AKUN BERHASIL DIBUAT =====")
        print(f"Nama         : {self.nama}")
        print(f"No Akun      : {self.nomor_akun}")
        print(f"Deposit Awal : Rp{self.saldo}")



    def deposit(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            self.riwayat.append(f"Deposit     : +Rp{jumlah}")  # Tambahan catatan transaksi ke riwayat
            print(f"\nDeposit berhasil sebesar Rp{jumlah}")
            print(f"Saldo saat ini : Rp{self.saldo}")
        else:
            print("Jumlah deposit tidak valid.")

    def tarik_tunai(self, jumlah):
        if 0 < jumlah <= self.saldo:
            self.saldo -= jumlah
            self.riwayat.append(f"Tarik Tunai : -Rp{jumlah}")  # Tambahan Tarik tunai Transaksi
            print(f"\nTarik tunai berhasil sebesar Rp{jumlah}")
            print(f"Sisa saldo : Rp{self.saldo}")
        else:
            print("Saldo tidak mencukupi atau jumlah tidak valid.")

    def cek_saldo(self):
        print(f"\nSaldo akun {self.nomor_akun} : Rp{self.saldo}")

    def lihat_riwayat(self):  # Tambahan Fungsi baru untuk menampilkan riwayat
        print(f"\n===== RIWAYAT TRANSAKSI AKUN {self.nomor_akun} =====")
        if not self.riwayat:
            print("Belum ada riwayat transaksi.")
        else:
            for i, transaksi in enumerate(self.riwayat, 1):
                print(f"{i}. {transaksi}")


def tampilan_awal():
    print("=" * 45)
    print("       SIMULASI BANK DIGITAL")
    print("=" * 45)

    input("\nTekan ENTER untuk memulai...")

    print("\nMemuat sistem", end="")

    for i in range(5):
        print(".", end="")
        time.sleep(0.5)

    print("\n")



def main():

    tampilan_awal()


    print("===== PEMBUATAN AKUN =====")

    nama = input("Masukkan nama nasabah : ")
    deposit_awal = float(input("Masukkan deposit awal : Rp"))

    akun = AkunBank(nama, deposit_awal)


    while True:

        print("\n===== MENU TRANSAKSI =====")
        print("1. Tarik Tunai")
        print("2. Cek Saldo")
        print("3. Deposit Lagi")
        print("4. Lihat Riwayat Transaksi")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")


        if pilihan == '1':

            while True:
                jumlah = float(input("\nMasukkan jumlah penarikan : Rp"))
                akun.tarik_tunai(jumlah)

                kembali = input(
                    "\nIngin tarik tunai lagi? (Ya/Tidak): "
                ).lower()

                if kembali != 'ya':
                    break


        elif pilihan == '2':

            while True:
                akun.cek_saldo()

                kembali = input(
                    "\nCek saldo lagi? (Ya/Tidak): "
                ).lower()

                if kembali != 'ya':
                    break


        elif pilihan == '3':

            while True:
                jumlah = float(input("\nMasukkan jumlah deposit : Rp"))
                akun.deposit(jumlah)

                kembali = input(
                    "\nIngin deposit lagi? (Ya/Tidak): "
                ).lower()

                if kembali != 'ya':
                    break

        elif pilihan == '4': #Tambahan
            while True:
                akun.lihat_riwayat()
                kembali = input("\nLihat riwayat lagi? (Ya/Tidak): ").lower()
                if kembali != 'ya':
                    break

        elif pilihan == '5':

            print("\nTerima kasih telah menggunakan layanan kami!")
            break

        else:
            print("Pilihan tidak valid.")



if __name__ == "__main__":
    main()