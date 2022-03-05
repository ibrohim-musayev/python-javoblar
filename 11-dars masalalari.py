# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 01:25:11 2022

@author: Ibrohim
"""

# 1-vazifa

cars={"model":"Ferrari", "rang": "Qora", "yili":1954}

#yangi fuftlik qo'shish
cars["egasi"]="Ibrohim"

print(cars["model"])
print(cars["rang"])




# 2-vazifa

otam={"ismi":"Eshmurod", 'tyili':1980, 'viloyat':'Surxondaryo'}
akam={'ismi':'O\'ktam', 'tyili':1994, 'viloyat':'Surxondaryo'}

print(f"Otamning ismi {otam['ismi']}, {otam['tyili']}-yilda {otam['viloyat']}da tug'ilgan")
print(f"Akamning ismi {akam['ismi']}, {akam['tyili']}-yilda {akam['viloyat']}da tug'ilgan")

dect={"apple":"olma", "blue": "Ko'k", "yellow":'sariq', 'car':'Mashina','dog':'it'}

typer=input("yozing: ").lower()
print(dect.get(typer,"BunSyo'q"))



# 3-vazifa

dic={"apple":"olma", "blue": "Ko'k", "yellow":'sariq', 'car':'Mashina','dog':'it'}

x=input("so'z kiriting: ").lower()

if x in dic:
    print(dic[x])
else:
    print('Bunda so\'z mavjud emas')
        

python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}
# print(python_izohli_lugati['tuple'])

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
     
    
    
    
    
    
    
    
    
    