"""
yazar: Zoda
tarih: 15.30 2/08/2021
çalışabilirlik: çalışabilir durumda
"""
yas = int(input("yaşınız:"))

if  yas < 18:
  print("on sekiz yaşından küçüksünüz")
elif 18 > yas:
  print("on sekiz yaşından büyüksünüz")
elif yas == 18:
  print("tam on sekiz yaşındasınız")
else::
  print("geçersiz bir yaş!")