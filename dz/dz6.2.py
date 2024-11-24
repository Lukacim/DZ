
seconds = int(input("Введіть кількість секунд: "))
days = seconds // 86400
hours = (seconds % 86400) // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
    day_word = "дні"
else:
    day_word = "днів"
print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
