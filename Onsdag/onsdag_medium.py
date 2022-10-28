lån = 500000
renteProsent = 4.5
rente = (renteProsent/100)+1

år = 10
måneder = år*12

avdrag = lån/år

def renteListe():
    for x in range(int(år)):
        renteSum = float(rente)**(x+1)
        renteSum = round(renteSum,4)
        lånSum = renteSum*lån
        print('År: ' + str(x+1) + ' || Rente: ' + str(renteProsent)+'%')
        print('Lån å betale: ' + str(round(lånSum, 1)) + 'kr\n')

def avdragListe():
    for x in range(måneder):
        lånbetalt = avdrag*(x+1)
        lånÅbetale = lånbetalt-lån
        print('Måned: ' + str(x+1) + ' || Avdrag: ' + str(avdrag))
        print('Lån Betalt: ' + str(round(lånbetalt)) + 'kr' + ' || Lån Å Betale: ' + str(abs(lånÅbetale)) + '\n')

def updateMåneder():
    global måneder
    måneder = int(år)*12

def nedbetalingsPlan():
    restlån = float(lån)-avdrag
    renterprosentert = renteProsent/100
    termin1renter = float(lån)*float(renterprosentert)
    renter = float(restlån)*float(renterprosentert)
    terminbeløp = renter+avdrag
    print('År: 1', '|| Restlån:', str(lån), '|| Renter:', str(termin1renter), '|| Avdrag:', str(avdrag), '|| Terminbeløp:', str(terminbeløp))

    for x in range(int(år)-1):
        print('År:', str(x+2), '|| Restlån:', str(restlån), '|| Renter:', str(renter), '|| Avdrag:', str(avdrag), '|| Terminbeløp:', str(terminbeløp))
        restlån = restlån-avdrag
        renter = restlån*renterprosentert
        terminbeløp = renter+avdrag
        
#!ikke mulig å lage diagram pga matplotlib funker ikke

def main():
    print('Lån:', str(lån) + 'kr || Rente:', str(renteProsent)+ '% || År:', str(år), '|| Måneder:', str(måneder))
    i = input('Skriv "1" for å endre Tall \nSkriv "2" for Rente Liste\nSkriv "3" for Avdrag Liste\nSkriv "4" for Nedbetalingsplan\n> ')
    if i == '1':
        endreTall()
        main()
    elif i == '2':
        renteListe()
        main()
    elif i == '3':
        avdragListe()
        main()
    elif i == '4':
        nedbetalingsPlan()
        main()
    else: 
        print('Ugyldig Operasjon, Prøv igjen.')
        main()

def endreTall():
    global lån
    global renteProsent
    global år
    global måneder
    global rente
    global avdrag
    
    i = input('Skriv "1" for å endre Lån\nSkriv "2" for å endre Rente\nSkriv "3" for å endre År\nSkriv "4" for å gå tilbake\n> ')
    if i == '1':
        lån = input('Skriv inn Lån: ')
        print('Lån nå:', str(lån) + 'kr') 
        avdrag = float(lån)/år
        endreTall()
    elif i == '2':
        renteProsent = input('Skriv inn Rente: ')
        rente = (float(renteProsent)/100)+1
        print('Rente nå:', str(renteProsent) + '%')
        endreTall()
    elif i == '3':
        år = input('Skriv inn År: ')
        updateMåneder()
        print('År nå:', str(år))
        endreTall()
    elif i == '4':
        print()
    else:
        print('Ugyldig Operasjon, Prøv igjen.')
        endreTall()
    
#---------------------------------------------

main()