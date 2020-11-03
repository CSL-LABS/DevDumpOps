# -*- coding: utf-8 -*-
from utils.Colors import Colors
import os
import requests
import signal

# paleta de colores
bc = Colors()

class Utils():
    def __init__(self):
        pass
    
    def createdFolders(self, path):
        dirs = ["", "/enumeration", "/dump"]
        for folder in dirs:
            ruta = path + folder
            if(not os.path.exists(ruta)):
                os.mkdir(ruta)

    def testVisibility(self, url, proxy):
        try:
            r = requests.get(url, proxies=proxy) 
            return True
        except requests.exceptions.SSLError:
            print(f"{bc.FAIL}[-] ERROR SSL: Invalid certificate{bc.ENDC}") # TODO: Agregar Flag y opcion
        except requests.exceptions.ProxyError:
            print(f"{bc.FAIL}[-] ERROR PROXY: No visibility!{bc.ENDC}")
        except requests.exceptions.ConnectionError:
            print(f"{bc.FAIL}[-] ERROR URL: No visibility!{bc.ENDC}")
        return False

    # Print iterations progress
    # Reference: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    def printProgressBar (self, iteration, total, prefix = '  [|] Progress:', suffix = 'Complete', decimals = 1, length = 50, fill = '█', printEnd = "\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
        # Print New Line on Complete
        if iteration == total: 
            print()