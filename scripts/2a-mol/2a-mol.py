#!/usr/bin/python36
#plus ou mois
#plus ou moins par fichier
#23/10
#Arnaud Dauguen


# I M P O R T
from random import randint


# F O N C T I O N S
#Ecriture
def writeInFile(to_write):
  file = open(path_file, "w")
  file.write(to_write)
  file.close()

#Lecture
def readInFile():
  file = open(path_file, "r")
  input = file.read()
  file.close()
  return input

#fct de check d'input d'un nombre
def inputNumber():
  number = 'typeHere'
  #si c'est pas un nombre on recommence
  while(number.isdigit() == False):
    number = readInFile()
    writeInFile('-___-')
  return int(number)

#fct qui return plus ou moins
def checkNumber():
  if (to_found == trying):
    done = True
    return 'gagné'
  elif (trying < to_found):
    return 'trop petit'
  else:
    return 'trop grand'


# V A R I A B L E S
path_file = '2a.txt'



done = False
to_found = randint(1, 100)
trying = -1


writeInFile('Bonjour, trouvez le nombre compris entre 1 et 100')

while (done == False and trying != to_found):
  trying = inputNumber()
  resultat = checkNumber()
  writeInFile(resultat)


