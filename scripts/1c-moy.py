#!/usr/bin/python36
# 1c-moy
# input pls note et prenom + affichage divers
# 15/10
# Arnaud Dauguen


# I M P O R T
import operator


# F O N C T I O N S
def selectNotes(dict):
  new_name = ' '
  new_note = 0
  while new_name != 'q':
    new_name = input('selectionnez un nom : ')
    if new_name != 'q':
      new_note = inputNote()
      dict[new_name] = new_note
  return dict


# fct de check d'input d'un nombre
def inputNote():
  note = input('type a number : ')
  # si c'est pas un nombre on recemmance
  while(note.isdigit() == False):
    note = input('type a true number : ')
  return int(note)


# affichage du top 5 et de la moyenne
def output(dict):
  nb_eleve = 0
  total_notes = 0
  # parcours des objet
  for name, note in dict.items():
    nb_eleve = nb_eleve + 1
    total_notes = total_notes + note
  print('moyenne de la classe : ' + str(calculerMoyenne(total_notes, nb_eleve)))
  print('le TOP 5 des notes')

  
  # trie du dico avec le second parametre, la note
  # reversed pour avoir en décroissant
  # et on affiche les 5 premiers
  print(sorted(dict.items(), key=operator.itemgetter(1), reverse = True)[:5])


def calculerMoyenne(total, nb):
  return(total / nb)  


# V A R I A B L E S
dict = {}


selectNotes(dict)
output(dict)
