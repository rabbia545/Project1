


# # def x ():
# #     print ("Hafiz, Where are you from?i am now in patharghata.")
# # x()



# # def teacher (id,name,designation="Development",salary=5000):
# #     return  id,name,designation,salary
# # print(teacher ( 55,"rab",))
# # print(teacher ( 55,"hafiz",))
# # print(teacher ( 55,"rokon",))
# # print(teacher ( 55,"antor",))





# def x (*args):
#     sum = 0
#     for result in args:
#         sum += result
#     return sum
# rab = x(35,175,52)
# print("rab your Total Amoount :",rab)


# # def my_function(x):
# #   return 5 * x

# # print(my_function(3))  
# # print(my_function(5))
# # print(my_function(9))



# def product (*args):
#     print(type(args))
#     sum = 0
#     for result in args:
#         sum += result
#     return sum
    
# rab = product (55,20,80,66)
# print("rab your total ammount is : ",rab)



# def y (*args):
#     sum = 0
#     for result in args:
#         sum += result
#     return sum
# hafiz = y (58,100,38,45)
# print("hafiz tumi emon koro keno:", hafiz)




# # def a(*args):
# #     sum=0
# #     for result in args:
# #         sum += result
# #     return sum
# # rokon=a(85,59,57,52)
# # print("basay gesila:", rokon)




# def f (**kwargs):
#     sum=0
#     for reuslt in kwargs:
#         sum += kwargs [reuslt]
#     return sum
# lajkl = f (lobon=35,cini=65,milk=60,semai=30) 
# print(lajkl)



# def hulk(**kwargs):
#     sum = 0
#     for result in kwargs:
#         sum+=kwargs[result]
#     return sum
# shulk = hulk(cini=65,tel=175,ata=100,syntax=65)
# print(shulk)






from keyword import kwlist


def iron (**kwargs):
    sum=0
    for result in kwargs:
        sum += kwargs[result]
    return sum
man = iron (hatur=50,loha=500,)
print(man)




def spider(**kwargs):
    sum=0
    for result in kwargs:
        sum += kwargs[result]
    return sum
man=spider(ghor=45,floor=60,height=1000,extra=46)
print(man)




product=lambda a,b,c : a+b+c
r = product(80,90,62)
print(r)