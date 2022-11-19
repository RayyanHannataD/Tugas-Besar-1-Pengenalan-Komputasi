daftar_nama = ["Nugget ayam", "Sosis ayam", "Sosis sapi", "Sayap ayam", "Bakso ikan", "Bakso ayam",
               "Siomay ayam", "Bakso udang", "Siomay udang", "Kentang goreng"]
daftar_harga = [10000, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000]
daftar_stok = [10, 18, 7, 6, 13, 9, 12, 20, 0, 3]
beli = True


def pilihan():
    print("1. Ya")
    print("2. Tidak")
    return


def bon(U, H, K):
    print("Transaksi berhasil")
    print("=======================================")
    print("Harga barang yang Anda pilih : Rp." + str(H))
    print("Uang yang Anda masukkan      : Rp." + str(U))
    print("Kembalian Anda sebesar       : Rp." + str(K))
    print("=======================================")
    return


def salam_tutup():
    print("=======================================")
    print("Terimakasih atas transaksi Anda")
    print("=======================================")
    return


def menu(i):
    print(str(i + 1) + ". " + daftar_nama[i] + ", Rp." + str(daftar_harga[i]) + ", Qty : " + str(daftar_stok[i]))
    return


pilihan()
X = int(input("Apakah Anda ingin menggunakan vending machine? "))

if X == 2:
    beli = False
while beli:  # looping selama 'beli' bernilai True
    lanjut = True
    print("=============DAFTAR BARANG=============")
    for i in range(10):
        menu(i)  # menampilkan menu
    print("=======================================")
    B = int(input("Silahkan pilih barang yang Anda inginkan : "))  # input barang yang diinginkan
    if B in range(1, 11):
        if daftar_stok[B - 1] == 0:  # cek jika barang yang dipilih memiliki stok/tidak
            pilihan()
            X = int(input("Stok barang yang Anda pilih telah habis. Apakah anda ingin memilih barang lain? "))  # user memillih untuk berhenti atau memilih barang baru
            if X == 2:
                beli = False  # jika user memilih berhenti, beli bernilai False
        else:
            for i in range(11):
                if B == i + 1:  # mencocokkan barang yang dipilih dengan indeks matriks
                    while lanjut:  # looping selama 'lanjut' bernilai True
                        H = daftar_harga[i]
                        print("=======================================")
                        U = int(input("Silahkan masukkan nominal uang sesuai barang yang Anda pilih : "))
                        print("=======================================")
                        if U > 0:  # cek jika nilai uang tidak valid
                            if U >= H:  # cek apakah uang cukup untuk membeli barang
                                K = U - H
                                daftar_stok[i] -= 1
                                bon(U, H, K)
                                pilihan()
                                X = int(input("Apakah Anda ingin melakukan transaksi lain? "))   # user memillih untuk berhenti atau memilih barang baru
                                if X == 2:
                                    lanjut = False  # jika memilih berhenti, 'beli' dan 'lanjut' bernilai False sehingga kedua loop berhenti
                                    beli = False
                                else:
                                    lanjut = False  # jika memilih untuk melakukan transaksi lain, maka 'lanjut' akan False sehingga kita akan kembali ke loop 'beli'
                            else:
                                pilihan()
                                X = int(input("Uang Anda tidak cukup. apakah Anda ingin melanjutkan transaksi? "))  # user memillih untuk berhenti atau memasukkan nilau uang yang lain
                                if X == 2:
                                    lanjut = False   # jika memilih berhenti, 'beli' dan 'lanjut' bernilai False sehingga kedua loop berhenti
                                    beli = False
                                else:
                                    beli = False  # jika ingin memasukkan nilai uang yang lain, hanya 'beli' yang bernilai False sehingga loop dimulai dari loop 'lanjut'
                        else:
                            print("Input tidak valid")
    else:
        print("=======================================")
        print("Input tidak valid")
else:
    salam_tutup()  # output bila transaksi sudah selesai
