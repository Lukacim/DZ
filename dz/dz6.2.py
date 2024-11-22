
seconds = int(input("Введіть кількість секунд: "))

if seconds < 0 or seconds >= 8640000:
    print("Число повинно бути від 0 до 8639999 включно.")
else:
    days = seconds // (24 * 60 * 60)
    remaining_seconds = seconds % (24 * 60 * 60)
    hours = remaining_seconds // (60 * 60)
    remaining_seconds = remaining_seconds % (60 * 60)
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60


    
    if days == 1:
        day_word = "день"
    elif 2 <= days <= 4:
        day_word = "дні"
    else:
        day_word = "днів"


    
    print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")


