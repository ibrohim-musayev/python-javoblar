# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     ism_yasa=f"{ism.title()} {familiya.title()}"
#     return ism_yasa

# talaba1=toliq_ism_yasa("Olim", "karimov")
# talaba2=toliq_ism_yasa("najim", "karimov")
# talaba3=toliq_ism_yasa("nazar", "karimov")
# talaba4=toliq_ism_yasa("kamol", "karimov")



# def darsga_kelmagan_talaba(ism, familiya, otasining_ismi=''):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         talaba_ismi=f"{ism} {familiya} {otasining_ismi}"
#     else:
#         talaba_ismi=f"{ism} {familiya}"
#     return talaba_ismi.title()
# talaba1=darsga_kelmagan_talaba("hasan", "karimov")
# talaba2=darsga_kelmagan_talaba("kamol","jamolov", "se")
# print(f"Darsga kelmagan talabalalar {talaba1} va {talaba2}")

# def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
#     """Avtomobel ma'lumotlari"""
#     avto={
#         'kompaniya':kompaniya,
#         'model':model,
#         'rangi':rangi,
#         'karobka':karobka,
#         'yili':yili,
#         'narh':narhi}
#     return avto
# avto1=avto_info("gm", "malibu", "qora", "mexanika", 2019)
# avto2=avto_info("porsche", "panamera", "qora", "avtomat", 2022, 150000)
# avtolar=[avto1,avto2]
# for avto in avtolar:
#     if avto['narh']:
#         narh=avto['narh']
#     else:
#         narh='Nomalum'
#     print(f"{avto['rangi']} {avto['model']}, narxi: {narh}")

# def oraliq(min,max):
#     """list di yorvoramiz"""
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min=min+1
#     return sonlar
# print(oraliq(10,20))


# def oraliq(min,max):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min=min+1
#     return sonlar
# print(oraliq(20,50))




# def oraliq(min,max, qadam):
#     sonlar=[]
#     if qadam:
#         while min<max:
#             sonlar.append(min)
#             min=min+qadam
#     else:
#          sonlar.append(min)
#          min+=1
#     return sonlar
# print(oraliq(5, 50, 5))






def avto_info(kompaniya, model, rangi, karobka, yili, narhi=None):
    """Avtomobel ma'lumotlari"""
    avto={
        'kompaniya':kompaniya,
        'model':model,
        'rangi':rangi,
        'karobka':karobka,
        'yili':yili,
        'narh':narhi}
    return avto

inf=avto_info("bmw", "range","qora",'avto',1998)
# print(avto_info("porsche", "panamera", "oq", "avtomat", 2022))

# print("saytimizdagi avtomobillar ro'yxatni shakklantiramiz!")
# avtolar=[]
# while True:
#     print("\nQuyidagi ma'lumotlarni kiritig!")
#     kompaniya=input("Ishlab chiqaruvchi:")
#     model=input("Modeli:")
#     rangi=input('Rangi:')
#     karobka=input("Karobka:")
#     yili=input("Ishlab chiqarilgan yili")
#     narhi=input("Narhi:")
#     avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))
#     javob=input("Yana avto qo'shasizmi (y/n)")
#     if javob=='n':
#         break
# print('Salonimizda mavjuda avtomobiullar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh=avto['narh']
#     else:
#         narh='Nomalum'
# print(f"{avto['rangi']} {avto['model']} narhi {narh}")





