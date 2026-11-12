import sys

dos = []
#buat loop
while True:
  print("""
  1.tambah teks
  2.liat teks
  3.hapus teks
  4.keluar

        """)

  msk = int(input("pilihan 1/2/3/4/ = "))
  # 1.tambah teks
  if msk == 1:
     masukan1 = input("tambahkan : ")
     dos.append(masukan1)
     print(f"tesk {masukan1} berhasil")

  elif msk == 2:
#buat dafta4 tugas
    if not dos:
      print("Daftar tugas masih kosong.")
    else:

      print("\nDaftar Tugas Anda:")
      for t, i in enumerate(dos,1):
        print(f"{t}. {i}")

  elif msk == 3:
     masukan3 = int(input("anka yang di hapus: "))
     masukan3 = masukan3-1

     if masukan3 not in dos :

       del dos[masukan3]
       vrbl = masukan3+1
       print("dihapus",vrbl)
       print(dos)

  elif msk == 4:
      print("keluar berhasil")
      sys.exit()

  else:
   print("kode tidak di terima")
   sys.exit()
