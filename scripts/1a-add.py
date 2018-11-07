#!/usr/bin/python36
# 1a-add
# afficher résultat de saisie x2
# 15/10
# Arnaud Dauguen


# I M P O R T
import re


# F O N C T I O N
def add(op1, op2):
  return op1 + op2


# fonction d'input, check number integre
def checkedInputNumber(patern):
  nb = input('type a number : ')
  while not patern.match(nb):
    nb = input('type a CORRECT number : ')
  return int(nb)


# V A R I A B L E
# regex pour detecter les nombres
patern = re.compile('^[0-9]+$')


nombreA = checkedInputNumber(patern)
nombreB = checkedInputNumber(patern)


print(add(nombreA, nombreB))
