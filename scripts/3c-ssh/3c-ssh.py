#!/usr/bin/python36
# 3a-save
# faire des backpus de repertoire
# 09/11
# Arnaud Dauguen


# C H E C K   M O D U L E S
  #bash : declare -r _tar=$(which tar 2> /dev/null) || { echo 'tar binary not found, exiting.' ; exit 2 ; }


import shutil
from shutil import make_archive
import os
import filecmp
import signal
import sys
import gzip
import argparse
from distutils.dir_util import copy_tree


# F O N C T I O N S
def saveDirectory(to_save, archive_name):
  make_archive(archive_name, 'gztar', to_save_path)


def checkExistingArchive():
  return os.path.exists(full_archive_path)


def moveArchiveTo(archive_file, backup_direcoty):
  if args.distant is False:
    shutil.move(archive_file, backup_directory)
  else:
  # connexion / transfert SSH
  if args.password and args.server and args.user:
    # connexion
    # j'ai fait la logique, woula le ssh j'arrive pas

def checkMoveFile():
  if checkExistingArchive() is True:
    # lire l'ancien backup
    with gzip.open(backup_directory + archive_file, 'rb') as f:
      old_save = f.read()
    # read le nouveau
    with gzip.open(archive_file, 'rb') as f:
      new_save = f.read()
  

    same_file = (old_save == new_save)
    # same_file sera tjr == False car le nouveau backup contient l'ancien
    # il faudrais save à l'exterrieur pour eviter ça mais ca marche donc voila


    if(same_file == False):
      sys.stdout.write('Saving new File in ' + backup_directory + '\n')
      os.remove(full_archive_path)
      moveArchiveTo(archive_file, backup_directory)
    else:
      os.remove(archive_file)
      sys.stdout.write('No need to backup \n')
  else:
    moveArchiveTo(archive_file, backup_directory)
    

# fct du ragequit CTRL+C
def ragequit(sig, frame):
  sys.stdout.write('-_______- \n')
  exit()


# I N T E R U P T
signal.signal(signal.SIGINT, ragequit)


# A R G U M E N T S
parser = argparse.ArgumentParser()
parser.add_argument("-b", "--backupLocation", type=str, help="choose directory to store backup (relative path)")
parser.add_argument("-d", "--directory", type=str, help="choose directories for backup, /!\ split with ',' (relative path)")
parser.add_argument("-u", "--user", type=str, help="type here you ssh user"
parser.add_argument("-p", "--password", type=str, help="type here you ssh password"
parser.add_argument("-s", "--server", type=str, help="type here you ssh serv asdress"
parser.add_argument("-d", "--distant" , help="active distant backup", action="store_true"
args = parser.parse_args()


# V A R I A B L E S
# installation des variables d'arguements
if args.backupLocation:
  backup_directory = str(args.backupLocation)
else:
  backup_directory = 'data/'


# on va s'occupper des dossiers en arg
if args.directory is False:
  to_save_path = '/root/B2-Python/scripts/'
else:
  to_save_path = 'temporaryFolder/'
  if os.path.isdir(to_save_path) is False:
    os.makedirs(to_save_path)
  for folders in args.directory.split(','):
    # on vire les '/' s'il y en a pour copy les dossier entiers
    folders.split('/')
    copy_tree(folders, to_save_path)


# variables standard
archive_name = 'backup'
archive_file = archive_name + '.tar.gz'
full_archive_path = backup_directory + archive_file
# verif de l'existance du dossier de backup
if os.path.isdir(backup_directory) is False:
  os.makedir(path_directory)


# appelle des fonctions


try:
  saveDirectory(to_save_path, archive_name)
  checkMoveFile()
  # delete tmp folder
  if args.directory:
    if os.path.isdir(to_save_path):
      shutil.rmtree(to_save_path)
except Exception as e:
  sys.stderr.write('y a u 1 pb`\n')
  sys.stderr.write(str(e) + '\n')
  pass


