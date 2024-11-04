weight_in_kg = int(input())
height_in_m = float(input())

if height_in_m != 0 and weight_in_kg != 0 :
    imt = weight_in_kg / height_in_m ** 2
else:
    print("Некорректні значення")

if imt < 18.5:
    print("Недостатня вага")
elif 18.5 <= imt <= 24.9:
    print("Нормальна маса тіла")
elif 25.0 <= imt <= 29.9:
    print("Зайва вага")
elif imt > 30:
    print("Ознаки ожиріння")
