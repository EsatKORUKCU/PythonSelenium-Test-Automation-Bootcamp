import time
 
ogrenciler=[]
while True:
  
  def ekle():
    ogrenci = input("Ögrenci ismini ve soyismini aralarında boşluk bırakarak giriniz  :")
    ogrenciler.append(ogrenci)
    print("işleminiz başarı ile gerçekleşti")
      
  def sil():
    ogren = input("Silinecek Ögrencinin ismini ve soyismini aralarında boşluk bırakarak giriniz  :")
    ogrenciler.remove(ogren)
    print("işleminiz başarı ile gerçekleşti")

  def multiekle():
    adet = int(input("Kaç adet ögrenci ekleyeceksiniz  : "))
    for i in range(adet):
        ogr = input("Ögrenci ismini ve soyismini aralarında boşluk bırakarak giriniz  :")
        ogrenciler.append(ogr)
    print("işleminiz başarı ile gerçekleşti")

  def multisil():
    adet = int(input("Kaç adet ögrenci sileceksiniz  : "))
    k = 1
    while k <= adet:
        sil()
        k += 1
    print("işleminiz başarı ile gerçekleşti")
        
  def listele():
    for liste in ogrenciler:
        print(liste)
    print("işleminiz başarı ile gerçekleşti")
        
  def numara():
    num = input("Numarası istenen Ögrencinin ismini ve soyismini aralarında boşluk bırakarak giriniz  :")
    for i in range(len(ogrenciler)):
        if(ogrenciler[i] == num):
            print("Sorgulanan ögrencinin numarası => " + str(i))
            print("işleminiz başarı ile gerçekleşti")
    
  print("Ogrenci Kayit Sistemi")

  print("1- Ogrenci Ekle") 
  print("2- Ogrenci Sil")
  print("3- Birden Fazla Ogrenci Ekle")
  print("4- Ogrencileri Listele")
  print("5- Ogrenci Numarasını Goster")
  print("6- Birden Fazla Ogrenci Sil")
  print("7-Cikis")
  
  sec=input("Lütfen bir seçim yapınız: ") 
  
  if sec=="1":
    ekle()
    time.sleep(2)
   
  elif sec=="2":
    sil()
    time.sleep(2)
    
  elif sec=="3":
     multiekle()
     time.sleep(2)
     
  elif sec=="4":
      listele()
      time.sleep(2)
  elif sec=="5":
    numara()
    time.sleep(2)
    
  elif sec=="6":
     multiekle() 
     time.sleep(2)
  else :
    break



    