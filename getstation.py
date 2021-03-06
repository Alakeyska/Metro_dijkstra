import requests
import json

stations_time = [
            ["Девяткино", "Гражданский проспект", 4],
            ["Гражданский проспект", "Академическая", 4],
            ["Академическая", "Политехническая", 2],
            ["Политехническая", "Площадь Мужества", 2],
            ["Площадь Мужества", "Лесная", 3],
            ["Лесная", "Выборгская", 3],
            ["Выборгская", "Площадь Ленина", 3],
            ["Площадь Ленина", "Чернышевская", 3],
            ["Чернышевская", "Площадь Восстания", 3],
            ["Площадь Восстания", "Владимирская", 2],
            ["Владимирская", "Пушкинская", 2],
            ["Пушкинская", "Технологический институт", 2],
            ["Технологический институт", "Балтийская", 2],
            ["Балтийская", "Нарвская", 3],
            ["Нарвская", "Кировский завод", 4],
            ["Кировский завод", "Автово", 2],
            ["Автово", "Ленинский проспект", 3],
            ["Ленинский проспект", "Проспект Ветеранов", 2],
            ["Парнас", "Проспект Просвещения", 3],
            ["Проспект Просвещения", "Озерки", 2],
            ["Озерки", "Удельная", 3],
            ["Удельная", "Пионерская", 3],
            ["Пионерская", "Чёрная речка", 3],
            ["Чёрная речка", "Петроградская", 4],
            ["Петроградская", "Горьковская", 2],
            ["Горьковская", "Невский проспект", 4],
            ["Невский проспект", "Сенная площадь", 2],
            ["Сенная площадь", "Технологический институт 2", 3],
            ["Технологический институт 2", "Фрунзенская", 2],
            ["Фрунзенская", "Московские ворота", 2],
            ["Московские ворота", "Электросила", 2],
            ["Электросила", "Парк Победы", 2],
            ["Парк Победы", "Московская", 3],
            ["Московская", "Звёздная", 4],
            ["Звёздная", "Купчино", 3],
            ["Беговая", "Новокрестовская", 3],
            ["Новокрестовская", "Приморская", 3],
            ["Приморская", "Василеостровская", 4],
            ["Василеостровская", "Гостиный двор", 4],
            ["Гостиный двор", "Маяковская", 3],
            ["Маяковская", "Площадь Александра Невского 1", 3],
            ["Площадь Александра Невского 1", "Елизаровская", 4],
            ["Елизаровская", "Ломоносовская", 3],
            ["Ломоносовская", "Пролетарская", 4],
            ["Пролетарская", "Обухово", 3],
            ["Обухово", "Рыбацкое", 4],
            ["Спасская", "Достоевская", 4],
            ["Достоевская", "Лиговский проспект", 2],
            ["Лиговский проспект", "Площадь Александра Невского 2", 4],
            ["Площадь Александра Невского 2", "Новочеркасская", 3],
            ["Новочеркасская", "Ладожская", 3],
            ["Ладожская", "Проспект Большевиков", 3],
            ["Проспект Большевиков", "Улица Дыбенко", 3],
            ["Комендантский проспект", "Старая Деревня", 4],
            ["Старая Деревня", "Крестовский остров", 3],
            ["Крестовский остров", "Чкаловская", 3],
            ["Чкаловская", "Спортивная", 2],
            ["Спортивная", "Адмиралтейская", 3],
            ["Адмиралтейская", "Садовая", 2],
            ["Садовая", "Звенигородская", 3],
            ["Звенигородская", "Обводный Канал", 3],
            ["Обводный Канал", "Волковская", 3],
            ["Волковская", "Бухарестская", 3],
            ["Бухарестская", "Международная", 3],
            ["Международная", "Проспект Славы", 2],
            ["Проспект Славы", "Дунайская", 3],
            ["Дунайская", "Шушары", 3],
            ["Технологический институт", "Технологический институт 2", 2],
            ["Пушкинская", "Звенигородская", 3],
            ["Владимирская", "Достоевская", 3],
            ["Площадь Восстания", "Маяковская", 3],
            ["Невский проспект", "Гостиный двор", 3],
            ["Сенная площадь", "Спасская", 3],
            ["Сенная площадь", "Садовая", 3],
            ["Площадь Александра Невского 1", "Площадь Александра Невского 2", 3]
            ]

def get_stations_nodes():
    url = 'https://api.hh.ru/metro/2'
    respon = requests.get(url)
    js = json.loads(respon.text)
    stations = []
    for line in [line["stations"] for line in js["lines"]]:
        for station in line:
            stations.append(station["name"])
    return stations