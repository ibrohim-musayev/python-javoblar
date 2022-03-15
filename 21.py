# def bahola(ismlar):
#     """baholaydigan funksiya"""
#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho=input(f"{ism.title()}ning bahosi nechi?")
#         baholar[ism]=int(baho)
        
#     return baholar
# talabalar=["ali","g\'ani","fotima","Jalol"]
# baholangan_t=bahola(talabalar[:])
# print(baholangan_t)


"""Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir 
matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing."""

# def katta_qil(matn):
#     natija=[]
#     while matn:
#         soz=matn.pop()
#         natija.append(soz.title())
#     return natija
# matnlar=['ali','jalil','kecha', 'kunduz']
# katta_harf=katta_qil(matnlar)
# print(katta_harf)

# def katta_harf(ismlar):
#     for n in range(len(ismlar)):
#         ismlar[n]=ismlar[n].title()
# talabalar=['ali','vali','kamol']    
# katta_harf(talabalar)
# print(talabalar)


"""Darsimiz davomida yozgan bahola funksiyasini .pop() 
metodidan foydalanmasdan va asl ro'yxatga o'zgartirish 
kiritmasdan faqat lug'at qaytaradigan qilib yozing."""


def bahola(talabalar):
    baholangan={}
    for ism in talabalar_bsiz:
        baholangan[ism]=int(input(f"{ism.title()} olgan bahosi:"))
    return baholangan
talabalar_bsiz=['ali','vali','kamol', 'malika']

print(bahola(talabalar_bsiz))










