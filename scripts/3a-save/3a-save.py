#!/usr/bin/python36
# 3a-save
# faire des backpus de repertoire
# 06/11
# Arnaud Dauguen


# C H E C K   M O D U L E S
  #bash : declare -r _tar=$(which tar 2> /dev/null) || { echo 'tar binary not found, exiting.' ; exit 2 ; }


import shutil
from shutil import make_archive
import os
import filecmp
import signal
import sys


# F O N C T I O N S
def saveDirectory(to_save, archive_name):
  make_archive(archive_name, 'gztar', to_save)


def checkExistingArchive():
  if (os.path.exists(full_archive_path)):
    return True
  else:
    return False


def moveArchiveTo(archive_file, backup_direcoty):
  shutil.move(archive_file, backup_directory)


def checkMoveFile():
  if checkExistingArchive() == True:
    same_file = filecmp.cmp(archive_file, full_archive_path)
    if(same_file == False):
      os.remove(full_archive_path)
      moveArchiveTo(archive_file, backup_directory)
    else:
      os.remove(archive_file)
  else:
    moveArchiveTo(archive_file, backup_directory)
    

# fct du ragequit CTRL+C
def ragequit(sig, frame):
  sys.stdout.write('-_______- \n')
  exit()


# I N T E R U P T
signal.signal(signal.SIGINT, ragequit)


# V A R I A B L E S
to_save_path = '/root/B2-Python'
archive_name = 'backup'
archive_file = archive_name + '.tar.gz'
backup_directory = 'data/'
full_archive_path = backup_directory + archive_file


# apelle des fonctions


try:
  saveDirectory(to_save_path, archive_name)
  checkMoveFile()
  sys.stdout.write('backup done, in ' + backup_directory + '\n')
except Exception as e:
  sys.stderr.write('y a u 1 pb`\n')
  sys.stderr.write(str(e) + '\n')
  pass
