# talaba = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }
# for key in set(talaba.values()):
#     print(key)    


# davlatlar = {
#     "o'zbekiston":'toshkent',
#     'aqsh':'washington d.c.',
#     'rossiya':'moskva',
#     'tojikiston':'dushanbe',
#     "qirg'iziston":'bishkek',
#     'qozog\'iston':'nursulton',
#     'malayziya':'kuala-lumpur',
#     'singapur':'sungapur',
#     'italiya':'rim'}
# davlat=input('Qaysi davlat poytaxtini bilishni xoxlaysiz?:>>>').lower()
# kdavlat=davlatlar.get(davlat)
# if kdavlat==None:
#     print("Sorry")
# else: print(kdavlat)

# mals=[]
# for n in range(10):
#     new_c={
#         'brand':None,
#         'motor':None,
#         'soni':40,
#         'narx':None}
#     mals.append(new_c)

# for carm in mals[:5]:
#     carm['brand']='BMW'
# for carm in mals[5:10]:
#     carm['brand']="MERS"
    
# for carm in mals:
#     if carm['brand']=="BMW":
#         carm['narx']=50000
#     else:carm['narx']=45000
    




# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#            }
# shaxslar=[buxoriy, qodiriy, vohidov, navoiy]

# for shaxs in shaxslar:
#     asar=shaxs['asarlar']
#     print(f"\n{shaxs['ism']}")
#     for asarlari in asar:
#         print(asarlari)



'''Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida 
   so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini
   esa ro'yxat ko'rinishida lug'artga saqlang. Natijani 
   konsolga chiqaring.'''
   
davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }

# for davlat, info in davlatlar.items():
#     if davlat=='aqsh':
#         davlat=davlat.upper()
#     else: davlat=davlat.capitalize()
    
#     print(f"{davlat}ning poytaxti {info['poytaxt']} shahri:"
#           f"Aholi soni {info['aholi']}"
#           )

# davlat=input("Qaysi davlat haqida ma'lumot olmoqchsiz?:").lower()
# if davlat in davlatlar:
#     info=davlatlar[davlat]
#     print(f"{davlat.capitalize()}ning poytaxti {info['poytaxt']} shahri:"
#           f"Aholi soni {info['aholi']}")