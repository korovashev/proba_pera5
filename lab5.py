def z1():
    country = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин",
     "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
     "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага",
     "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
     "Северная Македония": "Скопье", "Сербия": "Белград"}
    for key in country:
        print(key, ' - ', country[key])
    print()
    a = input('Введите страну: ')
    for key in country:
        if key == a:
            print(key, ' - ', country[key])
    print()
    for key in sorted(country):
        print(key, ' - ', country[key])

def z2():
    alp = {
        "авеинорст": 1,
        "дклмпу": 2,
        "бгёья": 3,
        "йы": 4,
        "жзхцч": 5,
        "шэю": 8,
        "фщъ": 10
    }
    sum = 0
    word = input('Введите слово: ').lower()
    for i in word:
        for key in alp:
            a = list(key)
            for j in a:
                if str(j) == str(i):
                    sum += int(alp[key])
    print('Сумма: ',sum)

def z3():
    students = {'Коровашев - русский, немецкий, французский',
        'Иванов - русский, японский, китайский'
    }
    languages = set()
    print('Фамилии тех, кто знает китайский язык: ', end='')
    for student in students:
        language = student.split(' - ')[1].split(', ')
        for i in language:
            if i == 'китайский':
                print(student.split(' - ')[0], end='')
        languages = languages.union(set(language))
    print('Языки: ', *sorted(list(languages)))
    print('Количество языков: ', len(list(languages)))
