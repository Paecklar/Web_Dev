print("Hallo\n")
print("Du hast den Meilenrechner gestartet.\n")
print("Mit diesem Programm kannst du von Kilometer in Meilen umrechnen, oder umgekehrt.\n")
Nochmal="Ja"
while Nochmal=="Ja"or Nochmal=="ja":
    Rechenrichtung = str(input("Bitte gib <km> ein, wenn du von km nach Meilen rechnen willst - sonst <m>\n"))
    if Rechenrichtung != "km" and Rechenrichtung != "m":
        print("Bitte gib nur km oder m ein!\n")
        continue
    elif Rechenrichtung == "m":
        print("Du willst von Meilen zu km rechnen\n")
    elif Rechenrichtung == "km":
        print("Du willst von km zu Meilen rechnen\n")
    Ausgangswert=float(input("Gib nun den Wert ein, den du umrechnen willst!\n"))
    if Rechenrichtung=="km":
        print(str(Ausgangswert) + "km sind " + str(Ausgangswert*0.621371192237334) + "Meilen")
    else:
        print(str(Ausgangswert) + " Meilen sind " + str(Ausgangswert/0.621371192237334) + "km")
    Nochmal=input("Willst du nochmal rechnen? Gib Ja oder Nein ein!\n")

