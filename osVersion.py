#!/usr/bin/python3

import argparse
import subprocess

# ingresar parametros de dominio o dirección IP

parser = argparse.ArgumentParser(description='Detectando la versión del OS')
parser.add_argument('-ip',dest="ip", help="127.0.0.1")

args = parser.parse_args()

#
def osDiscover(host=str(args.ip)):

    # enviar ping al target

    request = subprocess.run(['ping','-c 1',host],capture_output=True)

    if 'ttl=64' in str(request):

        print("[🐧] -> Linux" )


    elif 'ttl=127' or 'ttl=128' in str(request):
        print("🪟 -> Windows")
    
    else:
        exit(1) 

osDiscover()
