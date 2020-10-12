import os
import requests

class Utils():
    def __init__(self):
        pass
    
    def createdFolders(self, path):
        dirs = ["", "/enumeration", "/dump"]
        for folder in dirs:
            ruta = path + folder
            if(not os.path.exists(ruta)):
                os.mkdir(ruta)

    def testVisibility(self, url, proxy=None):
        try:
            r = requests.get(url, proxies=proxy) 
            return True
        except requests.exceptions.SSLError:
            print("Certificado autofirmado") # TODO: Agregar Flag y opcion
            return False
        except requests.exceptions.ConnectionError:
            print("ERROR: NO CONECTA")
            return False

    def testConection(self, target):
        # en cada modelo de target
        # agregar una propiedad de TEST
        # validar visibilidad a un ENDPOINT o RUTA
        pass 