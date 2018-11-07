#!/usr/bin/python36
# 1d-moy
# plus ou moins manuel
# 23/10
# Arnaud Dauguen


# F O N C T I O N S


# fct de check d'input d'un nombre
def inputNumber():
  number = 'typeHere'
  # si c'est pas un nombre on recommence
  while(number.isdigit() == False):
    number = input('type a true number : ')
    if(number == 'q'):
      goodbye()
  return int(number)


# fct qui return plus ou moins
def checkNumber(to_found, trying):
  if (to_found == trying):
    done = True
    return "gagné"
  elif (trying < to_found):
    return "trop petit"
  else:
    return "trop grand"


# fct d'au revoir
def goodbye():
  print('La solution était : ' + str(to_found) + '. Au revoir')
  exit()


# check ragequit CTRL + C
def quitting(sig, frame):
  goodbye()


# V A R I A B L E S
from random import randint
import signal
from time import sleep


done = False
to_found = randint(1, 100)
trying = -1


while (done == False and trying != to_found):
  signal.signal(signal.SIGINT, quitting)


  trying = inputNumber()
  print(checkNumber(to_found, trying))
