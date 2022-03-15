# ism=input("Ismingizni kiriting:")
# savol=f"Salom {ism.title()}, yoshingiz nechida?"
# yosh=input(savol)
# height="Bo'yingiz necha metr?"
# height=float(input(height))



# son=1
# while son<=5:
#     print(son, end=' ')
#     son+=1
# print('Ended')





# print("Istalgan sonning kvadratini aniqlovchi dastur!")
# savol="Istalgan sonni kiriting "
# savol+="dasturdan chiqish uchun 'exit' deb yozing!"
# qiymat=''
# while qiymat !='exit':
#     qiymat=(input(savol))
#     if qiymat!='exit':
#         print(float(qiymat)**2)
# print("Dasturdan chiqdingiz!")
 



# print("Istalgan sonning kvadratini aniqlovchi dastur!")
# savol="Istalgan sonni kiriting "
# savol+="dasturdan chiqish uchun 'exit' deb yozing!"
# ishora=True
# while ishora:
#     qiymat=input(savol)
#     if qiymat=='exit':
#         ishora=False
#     else:
#         print(f"{float(qiymat)**2}")
# print("Ended!")




# print("Istalgan sonning kvadratini aniqlovchi dastur!")
# savol="Istalgan sonni kiriting, "
# savol+="dasturdan chiqish uchun 'exit' deb yozing!"
# ishora=True
# while ishora:
#     son=input(savol)
#     if son=="exit":
#         break
#     else: 
#         print(f"{float(son)**2}")
# print("Ended!")


# sonlar=list(range(1,11))
# for son in sonlar:
#     if son==5:
#         continue
#     else:
#         print(son**2)

# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
# #         print(son)
# son=1
# while son<20:
#     son+=1
#     if son%2!=0:
#         continue
#     else:
#         print(son)


'"""AMALIYOT"""'
'''Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi
 stop so'zini yozishi bilan dasturni to'xtating'''
# kitoblar=[]
# qiymat=''
# while qiymat != 'exit':
#     qiymat=input("Yoqtirgan kitoblarinfiz:")
#     kitoblar.append(qiymat)
# print("Rahmat!")






'''Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga
 - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga 
 bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va
 chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
     *Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart 
tekshirish)'''
    
    
# savol="Yoshingiz nechida?"
# while True:
#     yosh=input(savol)
#     if yosh=="exit" or yosh=='quit':
#         break
#     yosh=int(yosh)
#     if yosh<7:
#         narh=2000
#     elif yosh<18:
#         narh=3000
#     elif yosh<65:
#         narh=10000
#     else: narh="bepul"
    
#     if narh==0:
#         print("Sizga kirish bepul!")
#     else: 
#         print(f"Sizga kirish {narh}")
# print("Rahmat!")

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")