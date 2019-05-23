Nochmal="Ja"
while Nochmal=="Ja":
    Erste = int(input("Gib die erste Zahl ein!\n"))
    Zweite = int(input("Gib die zweite Zahl ein!\n"))
    Operand = input("Gib den Operanden ein!\n")
    if Operand=="+":
        print(Erste + Zweite)
        Nochmal = input("Willst du nochmal?\n")
    elif Operand=="-":
        print(Erste - Zweite)
        Nochmal = input("Willst du nochmal?\n")
    elif Operand=="*":
        print(Erste * Zweite)
        Nochmal = input("Willst du nochmal?\n")
    elif Operand=="/":
        print(Erste / Zweite)
        Nochmal = input("Willst du nochmal?\n")
    else:
        print("Bitte gib nur +,-,* oder / ein!")
        Nochmal=input("Willst du nochmal?\n")