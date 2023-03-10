# # Задача
# num = int(input("Введите целое число ")) # 4
# data =[]
# while num != 0: # 4 !=
#     data.append(num) # data = [4]
#     num = int(input("Введите целое число ")) # 5
# data.sort()
# print(data)

#РАБОТАЕТ. МОЙ СКРИПТ.

print("Что надеть?")
temperature = input("Температура выше 20 градусов и меньше 30? (y/n) ")
inRain = None
if temperature == "y":
    inRain = input("Есть осадки? (y/n)")
    if inRain == "y":
        print("Футболку, шорты и дождевик.")
    else:
        print("Футболку и шорты.")
temperature = input("Температура выше 0 градусов? (y/n) ")
if temperature == "y":
    inRain = input("Есть осадки? (y/n)")
    if inRain == "y":
        inRain = input("Осадки сильные? (y/n)")
        if inRain == "y":
            print("Пальто, резинолвые сапоги и зонт.")
        else:
            print("Пальто и дождевик.")
    else:
        print("Пальто")
else:
    print("Пуховик")

# СКРИПТ ОТ ПЛАТФОРМЫ.

# temperature = int(input("Какая сейчас температура? "))
# rain = None
# heavyRain = None
#
# if temperature > 0:
#     rain = input("Идет дождь") == "да"
#     if rain:
#         heavyRain = input("Идет сильный дождь") == "да"
# decision = "Не решил что брать. Останусь дома."
# if 20 < temperature < 30:
#     if rain:
#         decision = "Взять футболку шорты и дождевик"
#     else:
#         decision = "Взять футболку и шорты"
# elif temperature > 0:
#     if rain:
#         if heavyRain:
#             decision = "Взять пальто, резиновые сапоги и зонт"
#         else:
#             decision = "Взять пальто и дождевик"
#     else:
#         decision = "Взять пальто"
# else:
#     decision = "Взять пуховик"










