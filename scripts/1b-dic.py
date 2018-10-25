#!/usr/bin/python36
#1b-dic
#input de noms et order
#15/10
#Arnaud Dauguen


# F O N C T I O N S
#input avec arret si q entré
def selectNames(list):
  new_name = input('selectionnez un nom : ')
  while new_name != 'q':
    list.append(new_name)
    new_name = input('selectionnez un nom : ')
  return list

def afficherList(list):
  for name in list:
    print(name)


# V A R I A B L E S
list = []


selectNames(list)
list.sort()
afficherList(list)
