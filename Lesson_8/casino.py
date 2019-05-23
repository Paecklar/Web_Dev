import random
Geheimzahl=random.randint(1,100)
Guess=Geheimzahl+1
Tipps=0
Guess = int(input("Gib deinen Tipp ein\n"))

while Geheimzahl!=Guess:
    if Guess<Geheimzahl:
        Guess=int(input("Tippe höher!\n"))
    else:
        Guess = int(input("Tippe niedriger!\n"))
    Tipps+=1

print("Super, du hast die Zahl erraten")
print("Du hast " + str(Tipps) + " Versuche gebraucht.")

