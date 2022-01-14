# # str2='let\'s play'
# # name1='Moshe'
# # age=24
# # string=f'{name1} is {age} years old'
# #
# # if age<29:
# #     print('is less')
# # else:
# #     print('29 or older')
# # cars=['suzuki','opel','kia']
# # for car in cars:
# #     print(car)
# #
# # count=0
# # while count<20:
# #     print(count)
# #     count=count+1
# # #  למצוא אות ברשימה
# # cars=['suzuki','opel','kia']
# #
# # for car in cars:
# #     for letter in car:
# #         if letter=='p':
# #             print(f'found {letter}')
# import random
#
# # num = '0123456789'
# # lower = 'abcdefghijklmnopqrstuvxyz'
# # upper = 'ABCDEFGHIJKLMNOPQURSTUVXYZ'
# # symbols = '!@#$%^&*()_-+=[]{}|\?/'
# #
# # all = num+lower+upper+symbols
# #
# # length = 16
# #
# # password = ''.join(random.sample(all,length))
# #
# # print(password)
#
# import random
#
# print(random.randint(2,4))
# print(random.randrange(7))
# range(0,10,2)
#
# # function
# cars=['suzuki','opel','kia'] #מיון רשימה
# print(max(cars))
# print(min(cars))
#
# sorted('Moshe')
# # הגדרת פונקציה
# def add(left=4,right=0):
#     return  left+right
#
# print (add(right=3))
# print()
# # len()
#
# # dictionary
# dict1={}
#
# dict2={'name':'dani','adult':True,'present':False}
# dict2['present']=True
# dict2['address']='Ramat Gan'
# print(dict2)
#
# dict2={'name':'dani','adult':True,'present':False}
# for key, value in dict2.items():
#     print(f'{key}={value}')
# print(type(x))
# if x > y:
#     x=5
# while y>2:
#     for x in y
# strip()
code = 'h7e4l3lo0768'
decode=[]
for n in code:
    if not n.isdigit():
        decode.append(n)
print(''.join(decode))
dict = {'num':1, 'num2':2, 'num3':3}
key='num'
def Dictonary():
    if key in dict: print('True')
    else: print('False')

Dictonary()
