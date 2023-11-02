from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Реалізуйте тут домашнє завдання

    # Отримуємо поточну дату
    today = date.today()
    print(users)

    # Створюємо словник для зберігання ім'я користувача за днем тижня
    birthdays_per_week = {}

    # Прапорець, що показує, чи знайдено користувачів для привітання
    found_users = False

    # Проходимося по користувачам і перевіряємо їхні дні народження
    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        # print(f" {name} : {birthday}")


        # Розраховуємо різницю між поточною датою та днем народження користувача
        days_until_birthday = (birthday - today).days
        # Перевірка, чи день народження випадає на суботу або неділю
        day_of_week = (today + timedelta(days=days_until_birthday)).strftime('%A')
        if day_of_week in ('Saturday', 'Sunday') and days_until_birthday > 0:
            # Якщо так, переносячи на понеділок
            day_of_week = 'Monday'
            # Додаємо ім'я користувача до відповідного дня тижня
            if day_of_week not in birthdays_per_week:
                birthdays_per_week[day_of_week] = [name]
            else:
                birthdays_per_week[day_of_week].append(name)
            found_users = True
            continue

        # Перевіряємо, чи день народження був минулого року
        if birthday.year < today.year:
            # Якщо так, переносимо його на наступний рік
            birthday = birthday.replace(year=today.year + 1)
            # Знаходимо день тижня для дня народження
            day_of_week = birthday.strftime('%A')
            if day_of_week not in birthdays_per_week:
                birthdays_per_week[day_of_week] = [name]
            else:
                birthdays_per_week[day_of_week].append(name)
            found_users = True
            continue

        # Якщо день народження наступного тижня і не випадає на вихідні, додаємо до відповідного дня тижня
        if 0 <= days_until_birthday <= 6:
            days_until_next_week = (days_until_birthday + today.weekday()) % 7
            # print(days_until_next_week)
            if days_until_next_week <= 4:
                day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'][days_until_next_week]
                # Додаємо ім'я користувача до відповідного дня тижня
                if day_name not in birthdays_per_week:
                    birthdays_per_week[day_name] = [name]
                    found_users = True
                else:
                    birthdays_per_week[day_name].append(name)



    # Повертаємо пустий словник, якщо не знайдено користувачів для привітання
    if not found_users:
        return {}

    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},


    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
