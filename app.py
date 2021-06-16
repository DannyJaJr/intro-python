# # # Number
# # my_variable = 5
# # print(my_variable)


# # # String
# # language = "Python"
# # print(language)

# # # Booleans
# # python_is_cool = True
# # javascript_is_better = False

# # # list
# # foods = ['burger', 'chesse', 'buns']
# # print(foods[1])
# # print(foods[-2])

# # print('----------')

# # for food in foods:
# #     print(food)

# #     print(len(foods))


# # cars = ['Mercedes', 'Audi', 'Jaguar']
# # for i in  car  enumerate(cars):
# # print('{}, {}' .format(i, car))

# # print('----------')

# teams = [ 'Clippers', 'Bucks', 'Nets', 'Jazz']
# for i in range(len(teams)):
#     each_team = teams[i]
#     print('{}. {}' .format(i, each_team))


# # print('----------')


# # Dictionaries
student = {
    "name":  'Danny',
    "class": 'Physics',
    "year": 2021,
}

# #Danny
# print(student["name"])
# #Physics
# print(student.get('class'))
# print('----------')
# for key in student:
#     print('{}, {}' .format(key, student[key]))

# print('----------')
# age = 22

# if age < 21:
#     print('Not old enough')
# elif age == 21:
#         print('You mad it')
# else:
#     print("You are old enough")

# print('----------')
# if student['name']:
#     print('{}' .format(student['name']))

# if 'James' in student.get('name'):
#     print(True)
# else:
#     print(False)

# print('----------')

# if 'Porsche' in cars:
#     print(True)
# else:
#     print(False)


def intro_student(name, course = 'Calculus', year = 2022):
    print('My name is {}. I am in {} class. I graduate in {}' .format(name, course, year)) 

# intro_student(student['name'], student['course'], student['year'])   
intro_student('Junior', 'Physics')


    
   

