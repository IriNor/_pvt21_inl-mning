correct_answers = 0
print("vad är Python?")
svaret = input(">>> Svaret är: ")
if svaret =="språk":
    print("Rätt!")
    correct_answers += 1
else:
    print("Fel! Rätt svaret: språk")
print("Vilken funktion används för att skriva ut saker på skärmen?")
svaret1 = input(">>> Svaret är: ")
if svaret1 == "print":
    print("Rätt!")
    correct_answers += 1
else:
    print("Fel! Rätt svar: print!")
print("Vilken funktion används för att mata in data ?")
svaret2 = input(">>> Svaret är: ")
if svaret2 == "input":
    print("input")
    correct_answers += 1
else:
    print("Fel! Rätt svar: input!")
print("Du fick " + str(correct_answers) + " av 3 rätt.")