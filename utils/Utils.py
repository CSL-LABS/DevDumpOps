import os
import requests
from utils.Colors import Colors

# paleta de colores
bcolors = Colors()

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
            print(f"{bcolors.FAIL}[*ERROR*] Verificacion SSL - Intenta desactivarla con verify=false{bcolors.ENDC}") # TODO: Agregar Flag y opcion
        except requests.exceptions.ProxyError:
            print(f"{bcolors.FAIL}[*ERROR*] Verifica el PROXY - No hay visibilidad!{bcolors.ENDC}")
        except requests.exceptions.ConnectionError:
            print(f"{bcolors.FAIL}[*ERROR*] Verifica la URL - No hay visibilidad!{bcolors.ENDC}")
        return False

    def testConection(self, target):
        # en cada modelo de target
        # agregar una propiedad de TEST
        # validar visibilidad a un ENDPOINT o RUTA
        pass 