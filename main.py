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