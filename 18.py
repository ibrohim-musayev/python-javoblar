# ismlar=[]
# print("Yaqin do'stlaringizni ro'yxatini tuzamiz!")

# n=1
# ishora=True
# while ishora:
#     savol=f"{n}-do'stingizni ismini kriting:"
#     ism=input(savol)
#     ismlar.append(ism)
#     takr=input("Yana boshqa ism qo'shasizmi? (ha/yo'q)")
#     if takr!="ha":
#         break
    
# print("Sizning do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# dostlar={}
# ishora=True
# while ishora:
#     ism=input("Do'stingizni ismini kiriting!")
#     yoshi=int(input(f"{ism.title()}ning yoshi nechida? "))
#     dostlar[ism]=yoshi
    
#     javob=input("Yana biror do'stingizni qo'shasizmi?")
#     if javob!='ha':
#         ishora=False
# print("Sizning do'stlaringiz!")
# for ism, yoshi in dostlar.items():
#     print(f"{ism.title()} {yoshi} yoshda!")


# cars=['lacetti', 'porsche','toyota' , 'nexia' , 'bmw' ,'gm' , 'nexia' ]
# car='nexia'
# while car in cars:
#     cars.remove(car)
# print(cars)

# cars=['lacetti', 'porsche','toyota' ]
# st_cars={}
# while cars:
#     car=cars.pop()
#     baho=input(f"{car.title()} testdan olgan bahosi:")
#     print(f"{car.title()} baholandi!")
#     st_cars[car]=float(baho)
    
    
'''Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar 
nomini birma-bir qabul qilib, yangi ro'yxatga joylang.'''

# buyurtmalar=[]
# n=1
# while True:
#     buyurtma=input(f"{n}-buyurtmangizni yozing!")
#     if buyurtma=='exit' or buyurtma=='quit':
#         break
#     else:
#         n+=1
#         buyurtmalar.append(buyurtma)
# print(buyurtmalar)


'''e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi
 dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va 
 uning narhi) kiritishni so'rang.'''
# e_bozor={}
# while True:
#     gro=input("Mahsulot nomini kiriting:")
#     price=input(f"{gro}ning narxi qancha?:")
#     e_bozor[gro]=float(price)
#     javob=input("Yana mahsulot qo'shazizmi? ha/yoq")
#     if javob!='ha':
#         break
# print(e_bozor)





buyurtmalar=['olma', 'anor', 'karam', 'sabzi']
mahsulotlar={
    "olma":2000,
    "sabzi":1500,
    "mango":9000,
    'sabzi':1500 }
while buyurtmalar:
    mahs=buyurtmalar.pop()
    if mahs in mahsulotlar.keys():
        narh=mahsulotlar[mahs]
        print(f"{mahs} - {narh} so'm")
    else:
        print(f"Bizda {mahs} yo'q!")
        
        