# talaba={
#         'ism':'Abdulloh',
#         'familiya':'shamsiyev',
#         'yoshi':24
#         }

# # print(talaba.items())

# for key, word in talaba.items():
#     print(f"key:{key}")
#     print(f"word:{word}")





# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'kanol':'iphone x',
#     'nilu':'galaxy s9',
#     'mam':'mi 10 pro',
#     'orafa':'nokia 3310'
#     }

# print("Foyfalanuvchilar quyidagi telfonlarni ishlatishadi")
# for ph in set(telefonlar.values()):
#     print(ph)
    
    
    

# for key, ph in telefonlar.items():
#     print(f"{key.title()}ning telefoni {ph}")
    

# mevalar={
#     'olma':20000,
#     'anor':8000,
#     'anjir':9000,
#     'banan':15000
#     }

# # print(mevalar.keys())
# print("Do'kondagi mahsulotlar:")
# for mahsulot in mevalar.keys():
#     print(mahsulot.title())

# bozorlik=['olma', 'anor', 'shaftoli']

# for meva in bozorlik:
#     if meva in mevalar:
#         print(f"{meva} narxi {mevalar[meva]} so'm")
#     if meva not in mevalar:
#         print(f"{meva} do'koningizga olib keling")

# print("Do'konimzdagi mahsulotlar")
# for meva in sorted(mevalar):
#     print(meva.title())

# print(telefonlar.values())












'''Masala javoblari'''

'''1-Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z 
qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida,
 alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.'''
 
py_lu = {'set':'unikallashtirish',
          'len':'uzunlikni o\'lchash',
          'title':'Bosh harfni kattalashtiradi',
          'upper':'barcha harflarni kattalashtiradi',
          'toople':'o\'zgarmas',
          'integer':'Butun son',
          'float': "O'nlik son",
          'boolean':"Mantiqiy qiymat",
          'for':"Biror amalni qayta-qayta bajarish tsikli",
        'if':'Shartlarni tekshirish operatori'}
for word, defe in sorted(py_lu.items()):
    print(word.title(),'-',defe)


'''2-Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi 
davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida 
konsolga chiqaring.'''


dp={'ozb':'toshkent',
    'kz':'olmota',
    'fr':'parij',
    'usa':'varshava'}
for dav in sorted(dp.keys()):
    print(dav.title())
print(' ')

for poy in sorted(dp.values()):
    print(poy.title())

'''Foydalanuvchidan istalgan davlatni kiritishni so'rang va 
shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi 
lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan 
xabarni chiqaring.'''



davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}

kirit=input("Davlat kiriting: ")
# if kirit in davlatlar:
#     print(davlatlar[kirit].title())
# else:
#     print("bizda bunday ma'lumotlar yo'q")

poytaxt=davlatlar.get(kirit)
if poytaxt==None:
    print("Bunday ma'lumot yo'q")
else:
    print(f"{kirit.title()}ning poytaxti {davlatlar[kirit].title()}")


'''Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini 
kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom 
menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q"
 degan xabarni chiqaring.'''
 
 
menu={
      'osh':20000,
      'manti':18000,
      'shorva':20000,
      'non':5000,
      'choy':5000}
buyurtmalar=[]
for buyurtma in range(3):
    buyurtmalar.append(input(f"{buyurtma+1}-buyurtmangizni kiriting:"))
    
for taom in buyurtmalar:
    if taom in menu:
        print(f"{taom}:{menu[taom]} so'm")
    else:
        print(f"Bizda {taom} yo'q!")