#!/usr/bin/python3

import os

# lista de directorios a crear
listDir = ['recenum','explotacion','privesc','notas']

# generar directorios -> os.mkdir()
def dirpent():
    for n in listDir:
        os.mkdir(n)

dirpent()
