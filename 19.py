# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("AssalomuAlaykum")
# salom_ber()

# def foydalanuvchi_yoshi(ism, yosh):
#     """Foydalanuvchi yoshini anqlovchi datsur"""
#     print(f"Foydalnuvchining ismi: {ism.title()}\n"
#           f"Foydalnuvchining ismi: {yosh}")
# foydalanuvchi_yoshi('Hasan',25)
# foydalanuvchi_yoshi(ism='kamol', yosh=25)

# def yosh_hisobla(son1, son2):
#     """Foydalnuvchi yoshinin hisoblavchi dastur!"""
#     if son1>son2:
#         print(f"{son1} {son2}dan katta")
#     elif son1<son2: 
#         print(f"{son1} {son2}dan kichik")
#     else:
#         print("Sonlar teng")
# yosh_hisobla(15,14)

print("Kiritilgan son 2 dan 10 gacha nechiga qoldizqsiz bo'linishini tekshiruvchi dastur")
def sonni_tekshir(son):
    """2 dan 10 gacha nechiga q.b.t.d"""
    for n in range(2,11):
        if son%n==0:
            print(f'{son} {n}ga qoldiqsiz bo\'linadi')
sonni_tekshir(20)