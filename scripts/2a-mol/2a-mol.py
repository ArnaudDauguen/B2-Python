#!/usr/bin/python36
# plus ou mois
# plus ou moins par fichier
# 25/10
# Arnaud Dauguen


# I M P O R T
from random import randint
import signal


# F O N C T I O N S
# Ecriture
def writeInFile(to_write):
  file = open(path_file, "w")
  file.write(to_write)
  file.close()


# Lecture
def readInFile():
  file = open(path_file, "r")
  input = file.readline().strip()
  file.close()
  return input


# fct de check d'input d'un nombre
def inputNumber():
  number = readInFile()
  #si c'est pas un nombre on recommence
  while(number.isdigit() == False):
    number = readInFile()
  return int(number)


# fct qui return plus ou moins
def checkNumber():
  if (to_found == trying):
    done = True
    return 'gagné'
  elif (trying < to_found):
    return 'trop petit'
  else:
    return 'trop grand'


# fct du ragequit CTRL+C
def ragequit(sig, frame):
  writeInFile('\n Pas sympa le ragequit -____-')
  exit()


# I N T E R U P T
signal.signal(signal.SIGINT, ragequit)


# V A R I A B L E S
path_file = "2a.txt"


done = False
to_found = randint(1, 100)
trying = -1


# pour indiquer le début de la partie
writeInFile('Bonjour, trouvez le nombre compris entre 1 et 100')


while (done is False and trying != to_found):
  trying = inputNumber()
  resultat = checkNumber()
  writeInFile(resultat)


