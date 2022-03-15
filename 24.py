import math
# uzunlik = lambda pi,r: 2*pi*r
# print(uzunlik(math.pi,5))

# kvadrat = lambda x, y : x**y
# print(kvadrat(9,2))




# def daraja(x):
#     t=x**2
#     return t

# kvadrat=daraja(2)

# def daraja(n):
#     return lambda x:x**n

# kvadrat=daraja(2)
# kub=daraja(3)
# print(kvadrat(9,10))

# from math import sqrt
# sonlar=list(range(11))
# ildizlar=list(map(sqrt,sonlar))
# print(ildizlar)
# def daraja2(x):
#     return x*x
# print(list(map(daraja2,sonlar)))

# kvadratlar=list(map(lambda x:x*2, sonlar))
# print(kvadratlar)

# a=[1,3,6]
# b=[9,7,4]
# plus=list(map(lambda x,y:x+y,a,b))
# print(plus)



# import random as r
# sonlar=r.sample(range(100), 10)
# print(sonlar)
# def juftmi(x):
#     return x%2==0
# juft_sonlar=list(filter(juftmi, sonlar))

# juft_sonlar=list(filter(lambda x:x%2==0, sonlar))
# print(juft_sonlar)


mevalar=['olma','anor',"o'rik",'shaftoli',"gilos"]
harf="s"
fltr=list(filter(lambda meva:meva.startswith(harf), mevalar))
# print(fltr)
kam5=list(filter(lambda meva:len(meva)<=5, mevalar))
# print(kam5)

yangi=list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
print(yangi)