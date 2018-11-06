#!/usr/bin/python36
#plus ou mois
#plus ou moins par fichier
#25/10
#Arnaud Dauguen


# I M P O R T
from random import randint
import signal


# F O N C T I O N S
#Ecriture
def writeInFile(to_write):
  file = open(path_file, "w")
  file.write(to_write)
  file.close()

#fct d'input d'un nombre
def getNewNumber(min, max):
  return int((max + min)  / 2)

#fct qui return plus ou moins
def checkNumber():
  if (to_found == trying):
    return 'gagné'
  elif (trying < to_found):
    return 'trop petit'
  else:
    return 'trop grand'

#fct du ragequit CTRL+C
def ragequit(sig, frame):
  writeInFile('\n Pas sympa le ragequit -____-')
  exit()


# I N T E R U P T
signal.signal(signal.SIGINT, ragequit)


# V A R I A B L E S
path_file = "2b.txt"
nbCoups = 0
min = 0
max = 100
resultat = 'WIP'
to_found = randint(min, max)
trying = -1


while (resultat != 'gagné' and trying != to_found):
  trying = getNewNumber(min, max)
  resultat = checkNumber()
  if(resultat == 'trop petit'):
    min = trying
  elif(resultat == 'trop grand'):
    max = trying

  print(trying)
  print(resultat)
  print(min)
  print(max)
  nbCoups += 1

#pour indiquer la fin de la partie
writeInFile('Le bot a trouvé en ' + str(nbCoups) + ' coups')
