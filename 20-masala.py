"""
Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, 
email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
"""

# def foydalanuvchi_ma(ismi, familiyasi, tug_y, tug_joyi, emaili, telf):
#     malumot={
#         'ismi':ismi,
#         'familiyasi':familiyasi,
#         "tug_y":tug_y,
#         "tug_joyi":tug_joyi,
#         "emaili":emaili,
#         "telf":telf}
#     return malumot
# foydalanuvchi_mal=[]
# while True:
#     ismi=input("Ismingizni kiriting:")
#     familiyasi=input("Famliyangizni kiriting:")
#     tug_y=int(input("Tug'ilgan yilingizni kiriting:"))
#     tug_joyi=input("Tug'ilgan joyingiz:")
#     emaili=input("Email manzilingiz:")
#     telf=input("Telefon raqamingizni kiriting:")
    
#     foydalanuvchi_mal.append(foydalanuvchi_ma(ismi, familiyasi, tug_y, tug_joyi, emaili, telf))
#     javob=input("Yana malumot kiritasizmi? (y/n)")
#     if javob!='y':
#         break
# print(foydalanuvchi_mal)
# for mal in foydalanuvchi_mal:
#     print(f"{mal['ismi'].title()} {mal['tug_y']}-yilda {mal['tug_joyi']}da tug'ilgan tel:{mal['telf']}")
    
"""Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va 
mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi 
ma'lumotni konsolga chiqaring."""


"""Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing"""
# def eng_k_aniqla(son1,son2,son3):
#     max = son1
#     if son2>=max:
#         max=son2
#     if son3>=max:
#         max=son3
#     return max
# print(eng_k_aniqla(23,65,89))
"""Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, 
diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing"""
# def aylana(radius):
#     aylana={
#         "radiusi":radius,
#         "diametri":2*radius,
#         "perimetri":2*3.14*radius,
#         "yuzi":4*3.14*radius}
#     return aylana

# aylana_m=[]
# while True:
#     radiusi=float(input("Aylana radiusiini kiriting:"))
#     aylana_m.append(aylana(radiusi))
#     javob=input("Yana ma'lumot qo'shasizmi? (y/n)")
#     if javob!="y":
#         break
# print(aylana_m)


"""Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya 
yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan 
katta musbat sonlar)"""

# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif(n==2):
#             tub = True
#         else:
#             for x in range(2,n):
#                 if(n%x==0):
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
                
#     return tub_sonlar

# print(tub_sonlar_top(11,199))
    
    
"""Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi 
ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing. Ta’rif: 
    Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan 
    ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had 
    ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,..."""

def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(0))





