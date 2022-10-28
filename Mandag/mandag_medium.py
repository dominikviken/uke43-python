import math

##Oppgave 1##
''' Hvis du  blir tilbudt 300 krone for å vaske et hus, ville du gjort det
da? hva om du ble tilbudt dette i 2 månader, hvor betalingen ville økes 15%
hver dag. Det vil si kr300 første dag, 345 andre dag, kr396.75 neste dag, osv.  '''

'''Lag en funksjon som regner ut total lønn etter 2 måneder, og lønn for 
dag 15, 30, 45 og 50. Bruk print() for å vise disse verdiene i terminalen'''

#mitt svar
kroner = 300
økning = 1.15

def oppgave1(dager):
  sum = kroner * (økning**dager)
  print(sum)

#oppgave1(15)
#oppgave1(30)
#oppgave1(45)
#oppgave1(50)

##Oppgave 2##
''' Opprett en funksjon som kan tegne følgende figur i terminalen:
*
**
***
****
*****
******
*******
********
*********
**********
***********
          *
         **
        ***
       ****
      *****
     ******
    *******
   ********
  *********
 **********
***********
'''

asterisk = '*'
space = ' '

def oppgave2():
  i=1
  y=11
  x=1
  
  for i in range(12):
    print(asterisk * i)

  for x in range(12):
    print((space * y) + asterisk * x)
    y-=1

oppgave2()

##Oppgave 3##
''' Opprett en funksjon som kan printe alle primtall i variabel prime_numbers '''
prime_numbers = [1, 5, 6, 7, 10, 11, 19, 23, 25, 26, 31, 26, 37, 40, 43, 67, 73, 99, 101]

def oppgave3():
  #for x in prime_numbers
    #del tall på 2
    #hvis tall får en desimal som ikke er 0
      #primtall
  pass