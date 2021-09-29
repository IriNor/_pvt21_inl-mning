import json

correct_answers = 0

json_data = None
with open("frågor_quiz.json", encoding="utf-8") as fd:
    json_data = json.load(fd)

qs = json_data['frågor']
ans = json_data['svar']

for key in qs:
    print(qs[key])
    my_ans = input('>> Skriv ditt svar här: ').strip().lower()
    if my_ans == ans[key]:
        correct_answers += 1
        print('Rätt!')
    else:
        print(f'Fel! Rätt svar är "{ans[key]}"')

print(f'Du har {correct_answers} poäng av 3 möjliga')