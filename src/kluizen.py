def toon_aantal_kluizen_vrij():
    bestand = open('kluizen.txt', 'r')
    regels = bestand.readlines()
    bestand.close()

    print('Er zijn nog {} kluizen vrij!'.format(12-len(regels)))


def nieuwe_kluis():
    beschikbarekluizen = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]

    bestand = open('kluizen.txt', 'r')
    regels = bestand.readlines()
    for regel in regels:
        kluisinfo = regel.split(';')
        kluisnummer = int(kluisinfo[0].strip())

        if kluisnummer in beschikbarekluizen:
            beschikbarekluizen.remove(kluisnummer)

    bestand.close()

    if len(beschikbarekluizen) > 0:
        kluiscode = input("Voer de kluiscode in voor uw nieuwe kluis: ")
        print('U krijgt kluis met nummer {} en code {}'.format(beschikbarekluizen[0], kluiscode))

        bestand = open('kluizen.txt', 'a')
        bestand.write("{};{}\n".format(beschikbarekluizen[0], kluiscode))
        bestand.close()
    else:
        print('Er is helaas geen kluis meer vrij!')


def kluis_openen():
    nummer = input('Wat is uw kluisnummer? ')
    code = input('Wat is uw kluiscode? ')

    bestand = open('kluizen.txt', 'r')
    regels = bestand.readlines()
    geopend = False
    for regel in regels:
        kluisinfo = regel.split(';')
        kluisnummer = kluisinfo[0].strip()
        kluiscode = kluisinfo[1].strip()

        geopend = (kluisnummer == nummer and kluiscode == code)
        if geopend:
            print('U heeft zojuist kluis {} geopend!'.format(kluisnummer))
            break

    if not geopend:
        print('Helaas, deze combinatie is niet correct!')


def kluis_teruggeven():
    nummer = input('Wat is uw kluisnummer? ')
    code = input('Wat is uw kluiscode? ')

    bestand = open('kluizen.txt', 'r')
    regels = bestand.readlines()
    teVerwijderen = None
    for regel in regels:
        kluisinfo = regel.split(';')
        kluisnummer = kluisinfo[0].strip()
        kluiscode = kluisinfo[1].strip()

        if kluisnummer == nummer and kluiscode == code:
            teVerwijderen = regel
            break

    if teVerwijderen is not None:
        regels.remove(teVerwijderen)

        bestand = open('kluizen.txt', 'w')
        for regel in regels:
            bestand.write(regel)
        bestand.close()
        print('Uw kluis is opgeheven!')
    else:
        print('Helaas, deze combinatie is niet correct!')


while True:
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
    print("2: Ik wil een nieuwe kluis")
    print("3: Ik wil even iets uit mijn kluis halen")
    print("4: Ik geef mijn kluis terug")
    print("5: Ik wil stoppen")

    keuze = eval(input("Uw keuze: "))
    if keuze == 1:
        toon_aantal_kluizen_vrij()
    elif keuze == 2:
        nieuwe_kluis()
    elif keuze == 3:
        kluis_openen()
    elif keuze == 4:
        kluis_teruggeven()
    elif keuze == 5:
        break
    else:
        print('Ongeldige keuze!')