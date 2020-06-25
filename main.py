import random
import time
# GALGJE

def beginning():
    print("Welkom\n")

    while True:
        name = input("Wat is je naam?\n").strip()

        if name == '':
            print("Heb je geen naam?")
        else:
            break

beginning()

def newFunc():
    print("Top! Dan gaan we galgje spelen!\n")

    while True:
        gameChoice = input("Wil je spelen?\n").upper()

        if gameChoice == "JA":
            break
        elif gameChoice == "NEE":
            print("Jammer! Fijne dag verder!")
            break
        else:
            print("Antwoord alleen met ja en nee")
            continue

newFunc()

#Laden
print ("Laden...")


#globale variabelen
woordenlijst = ['informatica','informatiekunde', 'spelletje','aardigheidje', 'scholier', 'fotografie','waardebepaling', 'specialiteit', 'verzekering',
'universiteit', 'heesterperk']
computerwoord = woordenlijst[random.randrange(0, 10)]


print ()
time.sleep(2)