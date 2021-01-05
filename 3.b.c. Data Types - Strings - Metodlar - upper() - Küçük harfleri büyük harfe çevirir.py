# upper()
# kod içersine yazılan harflerin büyük yazılmasını sağlar:
print("buraya yazılan harfler büyük harf olsun.".upper())
BURAYA YAZILAN HARFLER BÜYÜK HARF OLSUN.
# Parça parça da kullanılabilir:
print("buraya kadar yazılanlar büyük olsun".upper(),"burası küçük kalsın.")
BURAYA KADAR YAZILANLAR BÜYÜK OLSUN burası küçük kalsın.
# Bu metod bir değişkene de atanabilir:
isim = "gökay"
print(isim.upper())
GÖKAY
# HATIRLATMA: Değişkene atasam da değişkeni kalıcı olarak değiştirmez. Daha son-
# ra ben değişkeni yazdırmak istediğimde ilk haliyle aynen yazdırır:
print(isim)
gökay
# Ama yeni bir değişkene metodla beraber atarsak değişkeni yeni haliyle yazar:
yeni_isim = isim.upper()
print(yeni_isim)
GÖKAY
