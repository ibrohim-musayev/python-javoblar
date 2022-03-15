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


def avto_kirit():
    """Foydalanuvchidan olinadigan ma'lumotlar"""
    avtolar=[]
    while True:
        print("\nQuyidagi ma'lumotlarni kiritig!")
        kompaniya=input("Ishlab chiqaruvchi:")
        model=input("Modeli:")
        rangi=input('Rangi:')
        karobka=input("Karobka:")
        yili=input("Ishlab chiqarilgan yili")
        narhi=input("Narhi:")
        avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))
        javob=input("Yana avto qo'shasizmi (y/n)")
        if javob=='n':
            break


def info_print(avto_info):
    """Avtomobillar saqlangan funksiyani konsolga chiqaruvchi funksya:"""
    print(f"{avto_info['rangi'].title()} {avto_info['model']}, "
          f"Yili: {avto_info['yili']}")