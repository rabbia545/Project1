# # # List




# # student = ["Rab",918822,"Computer","hafiz",918784,"Computer","Rokon",133397,"Desktop"]

# # student [8] = "Computer"
# # print (student)


# # student.append ("Belal")
# # print (student)

# # student.insert (4,"hujur")
# # print (student)
# # student.extend (["Rokon","Desktop","dekhio","na"])
# # print (student)




# # # print (student[0:9])
# # # print (student[0:3])
# # # print(student[3:6])
# # # print(student[6:9])
# # # print (student [1])
# # # print (student)




# # # # # # tuple fixed

# # student = ("Rab", 918822, "Computer", "Rokon", 13397, "Computer", "Hafiz", 918784, "Computer")
# # print (student)





# ##### Set  v


# # teacher = {"Rab", 918822, "Computer", "Rab", 918822, "Computer", "Rab", 918822, "Computer", "Rab", 918822, "Computer",}
# # print (teacher)
# # # teacher[2] = "tech"
# # print(teacher)


# #####dicsonary

# student = {
#     "Name":"Rab",
#     "Dep":"Computer",
#     "Roll":918822
# }
# print(student["Roll"])
# print(student["Dep"])
# print(student["Name"])


from calendar import c


student = ["Rab", 918822, "Computer", "Rab", 13397, "Computer", "Rab", 918784, "Computer"]
for data in student:
    if data == "Rab":
        print (data)
    

c = student.count("Rab")
print (c)
