import json

with open('test.json', encoding='utf-8') as outfile:
    data = json.load(outfile)
    points = 0

    for i in range(0, len(data)):
        i += 1
        print(f'ВОПРОС №{i}')
        print(data[f"questions{i}"]["question"])
        right_answer = data[f"questions{i}"]["right_answer"]
        print('Правильный ответ: ', right_answer)
        for j in range(4):
            b = data[f"questions{i}"][f"answer_{j + 1}"]
            print(str(j + 1) + ' ' + b)
        answer = input('Введите номер правильного ответа: ')
        if answer == str(right_answer):
            points += 1
    print(f'Правильных ответов: {points}/15')
    print(f'В процентном соотношении: {round(points * 100 / 15)}%')
    if points > 8 or round(points * 100 / 15) > 60:
        print('Успешно')
    else:
        print('Вы провалились')
