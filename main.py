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

def game(): 

  #inleiding
  print("We gaan galgje spelen, kies een letter en raad het woord. Je hebt 5 beurten. Succes!")
  lengtewoord= len(computerwoord)
  temp= "." * lengtewoord
  print("het woord heeft " + str(lengtewoord) + " letters")
  
  #speler heeft 5 pogingen
  beurten= 5
  keuzes= ""
  
  while beurten > 0:
    beurt = 0
    for char in computerwoord:
        if char in keuzes:
          print(char,end="")
        else:
          print("_",end="")
          beurt +=1
    
    if beurt==0:
      print()
      print("Je hebt gewonnen")
      break
      print()
      print()
      print()
        
    kies = input("Kies een letter.")
    count2=0
        
    if len(kies)>1:
        telt2 +=1
        print("Je kan maar 1 letter kiezen")
    
    while telt2 >0:
      print("Je kan er maar 1 tegelijk kiezen")
      telt2 -= 1
      kies= kies.lower()
      keuzes += kies

    if kies not in computerwoord:
      beurten -=1
      print("Fout")
      print("Letters zover geraden",keuzes)
      print("Je hebt",+ beurten, 'meer keuzes')

      if beurten==0:
          print("Het woord was", computerwoord,"je hebt verloren")
  
      if kies in computerwoord:
        print("Goed")
        print("Letters zover geraden: ", keuzes)
        print("Je hebt", + beurten, 'meer keuzes')

beginning()
def newFunc():
   print("Top! Dan gaan we galgje spelen!\n")

   while True:
       gameChoice = input("Wil je spelen?\n").upper()
    
       if gameChoice == "JA":
         game()
         break
       elif gameChoice == "NEE":
           print("Jammer! Fijne dag verder!")
           break
       else:
           print("Antwoord alleen met ja en nee")
           continue
newFunc()

#globale variabelen
woordenlijst = ['informatica','informatiekunde', 'spelletje' 'aardigheidje', 'scholier', 'fotografie','waardebepaling' 'specialiteit', 'verzekering','universiteit', 'heesterperk']
computerwoord = woordenlijst[random.randrange(0, 11)]

print ()
time.sleep(2)
