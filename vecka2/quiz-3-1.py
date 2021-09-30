import json


def run():
    correct_answers = 0

    with open("quiz_3.json", encoding="utf-8") as file:
        quiz = json.load(file)
        qw = quiz["frågor"]

    for f in qw:
        print(f'\n1:{f["fråga"]} \n1. {f["1"]} \n2. {f["2"]} \n3. {f["3"]}')
        sva = input(">>> Svaret är: ")
        if sva == f[f["rätt_svar"]] or sva == f["rätt_svar"]:
            print("Rätt!")
            correct_answers += 1
        else:
            print(f'Fel! Rätt svar är {f[f["rätt_svar"]]}')

    print(f"\nDu fick {str(correct_answers)} poäng av {len(qw)}.")


if __name__ == '__main__':
    run()
