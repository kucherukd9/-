import json
from datetime import datetime, timedelta

FILE_NAME = "events.json"


def load_events():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_events(events):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=4, ensure_ascii=False)


def show_events(events):
    if len(events) == 0:
        print("Подій немає")
        return

    for i, event in enumerate(events):
        print(i + 1, event["name"], event["date"], event["time"], event["category"])


def add_event(events):
    name = input("Назва події: ")
    date = input("Дата (YYYY-MM-DD): ")
    time = input("Час (HH:MM): ")
    category = input("Категорія: ")

    new_event = {
        "name": name,
        "date": date,
        "time": time,
        "category": category
    }

    for event in events:
        if event["date"] == date and event["time"] == time:
            print("У цей час вже є подія")

    events.append(new_event)
    save_events(events)
    print("Подію додано")


def events_today(events):
    today = datetime.now().strftime("%Y-%m-%d")

    for event in events:
        if event["date"] == today:
            print(event)


def events_tomorrow(events):
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

    for event in events:
        if event["date"] == tomorrow:
            print(event)


def events_week(events):
    today = datetime.now()
    week = today + timedelta(days=7)

    for event in events:
        event_date = datetime.strptime(event["date"], "%Y-%m-%d")
        if today <= event_date <= week:
            print(event)


def delete_event(events):
    show_events(events)

    number = int(input("Номер події: ")) - 1

    if 0 <= number < len(events):
        events.pop(number)
        save_events(events)
        print("Подію видалено")


def edit_event(events):
    show_events(events)

    number = int(input("Номер події: ")) - 1

    if 0 <= number < len(events):
        event = events[number]

        name = input("Нова назва: ")
        date = input("Нова дата: ")
        time = input("Новий час: ")
        category = input("Нова категорія: ")

        if name != "":
            event["name"] = name
        if date != "":
            event["date"] = date
        if time != "":
            event["time"] = time
        if category != "":
            event["category"] = category

        save_events(events)
        print("Подію змінено")


def events_by_date(events):
    date = input("Введіть дату YYYY-MM-DD: ")

    for event in events:
        if event["date"] == date:
            print(event)


def help_menu():
    print("Команди:")
    print("додати")
    print("показати")
    print("тиждень")
    print("сьогодні")
    print("завтра")
    print("дата")
    print("редагувати")
    print("видалити")
    print("допомога")
    print("вийти")


def main():
    events = load_events()

    print("Вітаю. Я бот організатор подій.")
    help_menu()

    while True:

        command = input("Введіть команду: ").lower()

        if command == "додати":
            add_event(events)

        elif command == "показати":
            show_events(events)

        elif command == "тиждень":
            events_week(events)

        elif command == "сьогодні":
            events_today(events)

        elif command == "завтра":
            events_tomorrow(events)

        elif command == "дата":
            events_by_date(events)

        elif command == "видалити":
            delete_event(events)

        elif command == "редагувати":
            edit_event(events)

        elif command == "допомога":
            help_menu()

        elif command == "вийти":
            print("Програма завершена")
            break

        else:
            print("Невідома команда")


main()
