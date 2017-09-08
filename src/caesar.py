__author__ = 'jeroen.weber@hu.nl'


codetekst = 'Hi Fipkei dmnr hi hettivwxir zer eppiqeep, sqhex di lix zivwx zivamnhivh dmnr zer hi gypxyyv ir hi fiwglezmrk zer hi tvszmrgme ir iv wpiglxw diiv diphir osstpym hmrkir osqir fvirkir hmi fmnhvekir xsx hi zivaioipmnomrk zer lyr kiiwxir, ir sqhex di zpeo fmn hi Kivqerir pizir, hmi sziv hi Vmnr asrir ir qix ami di zssvxhyvirh ssvpsk zsivir.'
klaretekst = ''

def decodeer(ctekst,dist):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    lengte = len(ctekst)
    ktekst = ''
    for i in range(lengte):
        if (ctekst[i] != ' ' and ctekst[i] != ',' and ctekst[i] != '.'):
            pos = alfabet.index(ctekst[i]) - dist
            if (pos < 26 and ctekst[i] > 'Z'):
                pos += 26
            ktekst += alfabet[pos]
        else:
            ktekst += ctekst[i]
    return ktekst

klaretekst = decodeer(codetekst,4)
print(klaretekst)







