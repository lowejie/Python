# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it.")

# For loop from 1 till 19
# Function prints when i = 20

# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it.")
#
# my_function()
#
# # from random import randint
# # dice_images = ["1", "2", "3", "4", "5", "6"]
# # dice_num = randint(1, 6)
# # print(dice_images[dice_num])
#
# # Index range from 0 to 5
# # Randint returns 6 leads to exception
#
# from random import randint
# dice_images = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(1, 5)
# print(dice_images[dice_num])
#
# year = int(input("What's your year of birth?"))
#
# # if year > 1980 and year < 1994:
# #     print("You are a millennial.")
# # elif year > 1994:
# #     print("You are a Gen Z.")
#
# # 1994 as input prints nothing
# # If statement does not include 1994
#
# if year > 1980 and year <= 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")
#
#
# # Try Exception
# try:
#     age = int(input("How old are you?"))
# except ValueError:
#     print("You have typed in an invalid number. Please try again with numbers.")
#     age = int(input("How old are you?"))
# if age > 10:
#     print(f"You can drive at {age}.")
#
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# print(pages)
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)


import random
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
    b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])