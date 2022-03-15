"""1-usul *args"""
# def summa(*sonlar):
#     yigindi=0
#     for son in sonlar:
#         yigindi+=son
#     return yigindi
# print(1,2,3,4)


# def summa(x,y,*sonlar):
#     return x+y+sum(sonlar)
# print(summa(1,2,3,4))

"""2-usul *kwargs - keywods arguments"""

# def avto_info(kompaniya, model, **info):
#     """Avto haqida ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     info['kompaniya']=kompaniya
#     info['model']=model
#     return info
# avto1=avto_info('gm', 'malibu2', karobka='avtomat',yil=2021)
# avto2=avto_info('porsche', 911, probeg=0, rangi='oq')

"""Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi 
funksiya yozing"""
# def sonlar_k(*sonlar):
#     kopaytma=1
#     for son in sonlar:
#         kopaytma=kopaytma*son
#     return kopaytma
# print(sonlar_k(2,4,5))

"""Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi 
funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan 
ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin."""

def talabalar_haqida(ismi, familiyasi, **malumotlar):
    """Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi 
    funkisya"""
    malumotlar['ismi']=ismi
    malumotlar['familiyasi']=familiyasi
    return malumotlar
print(talabalar_haqida('hasan', "jabborov", yoshi=21, tug_joyi='Sirdaryo'))
    
    
    
    