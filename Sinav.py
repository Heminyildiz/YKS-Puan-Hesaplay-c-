print("YKS Puan Hesaplayıcı")
input("*****Başlamak için ENTER'a basınız*****")

adi = input("Adınız: ")
obp = int(input("OBP Puanınızı Giriniz: "))
print("-"*30)

while True:
    turkceD = int(input("Türkçe Doğrunuz: "))
    turkceY = int(input("Türkçe Yanlışınız: "))

    if int(turkceD) + int(turkceY) > 40:
        print("Doğru ve Yanlışlarınızın toplamı 40'tan büyük olamaz.")
    elif int(turkceD) + int(turkceY) <= 40:
        turkceN = int(turkceY) * 0.25
        turkceNet = float(turkceD) - float(turkceN)
        turkceP = float(turkceNet) * 3.3
        break
    else:
        print("Geçersiz Karakter")

print("-"*30)

while True:
    matD = int(input("Matematik Doğrunuz: "))
    matY = int(input("Matematik Yanlışınız: "))

    if int(matD) + int(matY) > 40:
        print("Doğru ve Yanlışlarınızın toplamı 40'tan büyük olamaz.")
    elif int(matD) + int(matY) <=40:
        matN = int(matY) * 0.25
        matNet = float(matD) - float(matN)
        matP = float(matNet) * 3.3
        break
    else: 
        print("Geçersiz Karakter")

print("-"*30)

while True:
    sosD = int(input("Sosyal Bilgiler Doğrunuz: "))
    sosY = int(input("Sosyal Bilgiler Yanlışınız: "))

    if int(sosD) + int(sosY) > 20:
        print("Doğru ve Yanlışlarınızın toplamı 20'den büyük olamaz.")
    elif int(sosD) + int(sosY) <= 20:
        sosN = int(sosY) * 0.25
        sosNet = float(sosD) - float(sosN)
        sosP = float(sosNet) * 3.4
        break
    else:
        print("Geçersiz Karakter")

print("-"*30)

while True:
    fenD = int(input("Fen Bilgisi Doğrunuz: "))
    fenY = int(input("Fen Bilgisi Yanlışınız: "))

    if int(fenD) + int(fenY) > 20:
        print("Doğru ve Yanlışlarınızın toplamı 20'den büyük olamaz.")
    elif int(fenD) + int(fenY) <= 20:
        fenN = int(fenY) * 0.25
        fenNet = float(fenD) - float(fenN)
        fenP = float(fenNet) * 3.34
        break
    else: 
        print("Geçersiz Karakter")

print("-"*30)

toplam = float(turkceNet) + float(matNet) + float(sosNet) + float(fenNet)

obpS = int(obp) * 0.6

hamPuan = float(turkceP) + float(matP) + float(sosP) + float(fenP) + 100
yerPuan = float(turkceP) + float(matP) + float(sosP) + float(fenP) + int(obpS) + 100
ham = float(turkceP) + float(matP) + float(sosP) + float(fenP)

print(f"Sayın {adi},\nToplam TYT Netiniz: {toplam}\nTYT Ham Puanınız: {hamPuan}\nTYT Yerleştirme Puanınız: {yerPuan} ")

input("*****AYT Puanınızı hesaplamak için ENTER'a basınız*****")

# input("Hesaplamak istediğiniz sınav türünü giriniz: ")
# Kullanıcıdan SAY-SÖZ-EA input'u al

while True:
    edD = int(input("Türk Edebiyatı Doğrunuz:  "))
    edY = int(input("Türk Edebiyatı Yanlışınız: "))

    if int(edD) + int(edY) > 24:
        print("Doğru ve Yanlışlarınızın toplamı 24'ten büyük olamaz.")
    elif int(edD) + int(edY) <= 24:
        edN = int(edY) * 0.25
        edNet = float(edD) - float(edN)
        edP = float(edNet) * 3.0
        break
    else:
        print("Geçersiz Karakter")

print("-"*30)

while True:
    mat2D = int(input("Matematik Doğrunuz: "))
    mat2Y = int(input("Matematik Yanlışınızı Giriniz: "))

    if int(mat2D) + int(mat2Y) > 40:
        print("Doğru ve Yanlışlarınızın toplamı 40'tan büyük olamaz.")
    elif int(mat2D) + int(mat2Y) <= 40:
        mat2N = int(mat2Y) * 0.25
        mat2Net = float(mat2D) - float(mat2N)
        mat2P = float(mat2Net) * 3.0
        break
    else:
        print("Geçersiz Karakter")

print("-"*30)

while True:
    t1D = int(input("Tarih-1 Doğrunuz: "))
    t1Y = int(input("Tarih-1 Yanlışınız: "))

    if int(t1D) + int(t1Y) > 10:
        print("Doğru ve Yanlışlarınızın toplamı 10'dan büyük olamaz. ")
    elif int(t1D) + int(t1Y) <= 10:
        t1N = int(t1Y) * 0.25
        t1Net = float(t1D) - float(t1N)
        t1P = float(t1Net) * 2.80
        break
    else:
        print("Geçersiz Karakter")

print("-"*30)

while True:
    c1D = int(input("Coğrafya-1 Doğrunuz: "))
    c1Y = int(input("Coğrafya-1 Yanlışınız: "))

    if int(c1D) + int(c1Y) >6:
        print("Doğru ve Yanlışlarınızın toplamı 6'dan büyük olamaz.")
    elif int(c1D) + int(c1Y) <=6:
        c1N = int(c1Y) * 0.25
        c1Net = float(c1D) - float(c1N)
        c1P = float(c1Net) * 3.33
        break
    else:
        print("Geçersiz Karakter")

print("-"*30)

tytSon = float(ham) * 0.4

tmPuan = float(edP) + float(mat2P) + float(t1P) + float(c1P) + float(tytSon) + int(obpS) + 100
print(f"Sayın {adi}, YKS Puanınız: {tmPuan}")

# Bu noktadan sonra SAY ve SÖZ AYT eklenecek.