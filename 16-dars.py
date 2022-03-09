# malibus=[]
# for n in range(10):
#     new_car={
#         'model':'ls',
#         'rang':None,
#         'yil':2022,
#         'narh':None,
#         'km':0,
#         'karobka':'avtomat'}
#     malibus.append(new_car)
# for malibu in malibus[:3]:
#     malibu['rang']='qizil'
    
# for malibu in malibus[3:6]:
#     malibu['rang']='qora'
    
# for malibu in malibus[6:]:
#     malibu['rang']='qora'
#     malibu['karobka']=['mexanika']

# for malibu in malibus:
#     if malibu['karobka']=='avtomat':
#         malibu['narh']=40000
#     else:
#         malibu['narh']=35000
        
# for malibu in malibus:
#     print(malibu)
    

# dasturchilar={
#     'ali':['C++','C#'],
#     'hasan':['Python','JS'],
#     'kamol':['C++','python'],
#     'nari':['C++','C#',"Node.JS"],
#     'jamshid':['C++','Unity'],
#     'ibo':['C++','Kotlin']
#     }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end="")
#     for til in tillar:
#         print(f"{til.upper()} ", end="")



# hamkasblar={
#     'ali':{
#         'familiya':'karimov',
#         'tyili':1994,
#         'malumot':'oliy',
#         'tillar':["C++","node.js"]},
#     'hasan':{
#         'familiya':'narimonov',
#         'tyili':1997,
#         'malumot':'oliy',
#         'tillar':["C++","node.js"]},
#     'nodir':{
#         'familiya':'nazarov',
#         'tyili':2000,
#         'malumot':'oliy',
#         'tillar':["C++","node.js"]}
#     }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}",
#           f"\n{info['tyili']}-yilda tug'ilgan",
#           f"\nMalumoti: {info['malumot'].title()}\n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())



# AMALIYOT

'''- Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur 
    shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. 
    Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi 
    ma'lumotni konsolga chiqaring.'''
    
# tolstoy={
#     'ismf':'hasanov abdullohh behbudiy',
#     'tyili':1987,
#     'asarlari':'hasan va husan',
#     'vafoty':2034}
# jamshid={
#     'ismf':'hasanov abdullohh behbudiy',
#     'tyili':1987,
#     'asarlari':'hasan va husan',
#     'vafoty':2034}
# hakam={
#     'ismf':'hasanov abdullohh behbudiy',
#     'tyili':1987,
#     'asarlari':'hasan va husan',
#     'vafoty':2034}
# vzam=[tolstoy, jamshid, hakam]
# for mashxur in vzam:
#     print(f"{mashxur['ismf'].title()}, "
#           f"{mashxur['tyili']}-yilda tug'ilgan, "
#           f"{mashxur['asarlari'].title()} asarlari muallifi")
    
    
''''- Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari
 ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi 
 va uning asarlarini konsolga chiqaring.

- Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali 
    haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini
    esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.

- Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar 
haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida
 ma'lumotni konsolga chiqaring.
'''

davlatlar={
    'ozbekiston':{
        'poytaxti':'toshkent',
        'maydoni':'447ming.kv.km',
        'aholisi':'30mln'},
    'kazak':{
        'poytaxti':'almata',
        'maydoni':'1mln.kv.km',
        "aholisi": '15mln'},
    'tajik':{
        'poytaxti':'nonee',
        'maydoni':'1mln.kv.km',
        "aholisi": '15mln'},
    "aqsh":{
        'poytaxti':"vashington",
        'maydoni':'9mln.kv.km',
        'aholisi':'327 mln',}
    }

# for davlat, info in davlatlar.items():
#     if davlat.lower()=='aqsh':
#         davlat=davlat.upper()
#     else: 
#         davlat=davlat.capitalize()
#     print(f"{davlat}ning poytaxti {info['poytaxti'].title()}, "
#           f"aholi soni {info['aholisi']}, "
#           f"maydoni {info['maydoni']}")
'''
- Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni 
emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar 
davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida
 ma'lumot yo'q" degan xabarni chiqaring.'''


kdavlat=input("Davlat kiriting: ")
if kdavlat.lower() in davlatlar:
    print(f"{davlatlar['kdavlat'].title()}ning poytaxti {info['poytaxti'].title()}, "
              f"aholi soni {info['aholisi']}, "
              f"maydoni {info['maydoni']}")
else:
    print("Bizda bunday ma'lumotlar yo'q!")
    
    
            