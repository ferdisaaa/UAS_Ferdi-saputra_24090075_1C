while True:
  nim = input("masukkan nim: ")
  nama = input("masukkan nama: ")

  print ("Nomor Nim",nim,"Dengan nama",nama)

  ulangi = input("Apakah anda ingin melanjutkan? y/t?")

  if ulangi == "y":
    continue
  elif ulangi == "t":
    print("terimakasih")
    break
  else:
      print("maaf, inputan yang kamu masukkan tidak sesuai!")
      ulangi = input("Apakah anda ingin menambahnya? y/t?")
  if ulangi == "y":
    continue
  elif ulangi == "t":
    print("terimakasih")
    break


    

