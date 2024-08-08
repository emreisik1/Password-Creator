import random
import string

karakter = string.ascii_letters + string.punctuation + string.digits
uzunluk = int(input("İstediginiz uzunlugu giriniz."))
sifre = "".join(random.choice(karakter) for x in range(uzunluk))

print(sifre)