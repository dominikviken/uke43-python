import random as rn
import pygame as pg
import sys

## Oppgave 1##
pg.init()

w = 600
h = 650

background = pg.display.set_mode((w, h))
pg.display.set_caption =('Oppgave_medium')
pg.display.flip()

a = rn.randint(1,30)
b = rn.randint(30,40)
coord1=(a,b)

'''
Variablene a og b inneholder tilfedige verdier mellom 1 og 30 (a), og mellom 30 og 40 (b). Variabelen coord1
inneholder verdiene av a og b. 

Opprett en funksjon som kan tegne tilfeldige figurer. For å løse denne oppgaven må du lage flere variabler som 
brukes som koordinate-punkter for å tegne figurer for eksempel:

'''

running = True

# Main loop
while running:
    #tegn figurer her
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()