# import math
# # x = 400
# # print(math.sqrt(x))
# # print(math.pow(5, 3))
# # print(math.pi)
# # print(math.log2(8))




import random as r

"""randint()"""
# son=r.randint(0, 1000)
# print(son)

"""choice()"""
# ismlar=[2,4,5,7]
# ism=r.choice(ismlar)
# print(ism)

# print(r.choice(ism))  """harfni oladi"""

# x=list(range(0,51,5))
# print(x)
# print(r.choice(x))

"""shuffle() - aralshtirib tashlash"""
x=list(range(11))
print(x)
r.shuffle(x)
t=x[:]
print(t)
son=r.choice(t)
print(son)
