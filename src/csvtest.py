__author__ = 'jeroen.weber@hu.nl'

__author__ = 'jouke-bouwe'

import csv

csvKlantBestand = 'klantBestand.csv'

#variablen voor het registreren en opslag
email = ""
naam = ""
achternaam = ""
wachtwoord = ""
wachtwoord2 = ""

#variablen voor het inloggen van de user
inlogEmail = ""
inlogWachtwoord = ""

fieldnames = ["email", "wachtwoord", "naam", "achternaam"]

#In deze functie slaan we de gegevens van de klant op in een csv bestand.
def registreren(email, wachtwoord, naam, achternaam):

    email = input("Vul hier je e-mail adress in")
    wachtwoord = input("Vul hier je wachtwoord in")
    wachtwoord2 = input("Vul hier je wachtwoord in ter controle")
    naam = input("Vul hier je naam in")
    achternaam = input("Vul hier je achternaam in")

    if wachtwoord == wachtwoord2:
        try:
            klantBestand = open(csvKlantBestand, 'a', newline='')
            writer = csv.DictWriter(klantBestand,delimiter=',', fieldnames=fieldnames)
            writer.writerow({"email": email, "wachtwoord": wachtwoord, "naam":naam, "achternaam": achternaam})
        finally:
            klantBestand.close()
    else:
        print("Wachtwoord komt niet overeen")


def leesUit():

    inlogEmail = input("Geef je e-mail")
    inlogWachtwoord = input("Geef je wachtwoord")

    try:
        leesKlantUit = open(csvKlantBestand, 'r')
        reader = csv.DictReader(leesKlantUit, delimiter=',')

        for row in reader:
            if row["email"] == inlogEmail and row["wachtwoord"] == inlogWachtwoord:
                print("Inloggen is een succes!")
            else:
                print("Inloggen is niet gelukt")

    finally:
        leesKlantUit.close()

registreren(email, wachtwoord, naam, achternaam)
leesUit()


