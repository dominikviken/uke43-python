import numpy as np
#import matplotlib as plt

word1 = 2
word2 = 4
word3 = 6
word4 = -2
word5 = 10

## Oppgave 1##

'''
Opprett en while loop som kan:

1.-Opprett en lista med de variablene ovenfor 
2.-Summere verdien til alle variablene
3.-Printe verdien i terminalen.

'''

def oppgave1():
    while True:
        wordlist = [word1, word2, word3, word4, word5]
        g = sum(wordlist)
        print(str(g))

#oppgave1()

## Oppgave 2##

'''
finn en funksjon (Det finnes flere) som printer variablene ovenfor sortert fra det minste til det største. 
'''

def oppgave2():
    wordlist = [word1, word2, word3, word4, word5]
    wordlist.sort()
    print(wordlist)

#oppgave2()

## Oppgave 3##

countries  = ["Nicaragua", "Cuba", "Kina", "Østerrike", "Nederland", "Norge", "Chile", "Brasil","Venezuela"]
konsumprisindeks = [3.4, 1.2, 3.7, 5.3, 4.9, 6.9, 8.1, 7.2, 3.4 ]
colors = [ "yellow", "red", "blue", "silver", "deeppink", "brown", "grey", "cyan", "darksalmon"]

'''
lag en diagram (pie type) som viser elementene til variabel "countries" og kunsumprisindeks med farge. 

'''

#fig = plt.figure(figsize =(10, 7))
#plt.pie(konsumprisindeks, labels = countries)

#plt.show()

#! får error #No module named 'matplotlip', men jeg har matplotlip installert 

## Oppgave 4##


'''
Lag en while loop som legger til tall fra 0 til 50. Deretter må løkken summere alle elementene. Opprett en ny variabel 
som tar imot resultatet til forrige operasjonen. Bruk print() for vise vedien til den nye variabelen.

'''

seat_number = []

def oppgave4():
    i = 1
    while True:
        seat_number.insert(i, i)
        i = i + 1
        result = sum(seat_number)
        if i == 51: 
            result = sum(seat_number)
            print(result)
            break
        
#oppgave4()
## 