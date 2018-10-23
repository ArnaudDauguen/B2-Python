#!/usr/bin/python36
#titre
#desc
#15/10
#Arnaud Dauguen


# F O N C T I O N S

#fct de check d'input d'un nombre
def inputNote():
  in = input('type a number : ')
  #si c'est pas un nombre on recommence
  while(in.isdigit() == False):
    in = input('type a true number : ')
  return int(in)

# V A R I A B L E S
