# Web API - SonarQube
# https://sonarcloud.io/web_api/

import requests

import math
import os
from model.Sonar import Sonar
from controller.SonarQube.Recon import Recon
from utils.Colors import Colors

# paleta de colores
bcolors = Colors()

class SonarController():
    def __init__(self, url, authorization, output):
        self.path = output
        self.url = url
        self.sonar = Sonar(url, authorization[0])
        self.sReq = requests.Session()

        if(authorization[1]):
            self.sReq.headers.update({"Authorization": "Basic " + authorization[0]})
        
        Recon(url, self.sReq, output)
    
    def enumeration(self):
        #logica - enumeracion
        pass

    def dump(self, output):
        #logica - DUMP
        self.getOrganizations()
        self.getComponents()
        cont = 0
        print(f"{bcolors.OKGREEN}[+] Dumpeando todos los archivos....{bcolors.ENDC}")

        for component in self.sonar.components: 
            cont += 1
            key = component["key"]
            tmpPath = (component["organization"] + "/" + key.replace(":","/")).split("/")
            tmpPath.pop()
            localPath = output + "/".join(tmpPath)

            if not os.path.exists(localPath):
                os.makedirs(localPath)
            self.getSourceRaw(key, localPath + "/" + component["name"])

        print(f"{bcolors.WARNING}[+] >>> Archivos Descargados completamente....{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}[+] Se descargaron {cont} archivos, de {len(self.sonar.organizations)} organizaciones....{bcolors.ENDC}")
        print(f"{bcolors.OKBLUE}[+] Resultados almacenados en {output}....{bcolors.ENDC}")
    
    # Descarga codigo por key
    def getSourceRaw(self, key, path):
        # TODO: ¿los archivos antiguos?
        # ¿¿cada version sera un proyecto diferente?? 
        # o debo validar que no este sobreescribiendo archivos
        endpoint = self.url + "api/sources/raw?key="
        data = self.sReq.get(endpoint + key)

        with open(path, "wb") as f:
            f.write(data.content)
    
    # Lista todas las organizaciones
    def getOrganizations(self):
        print(f"{bcolors.OKGREEN}[+] Enumerando las organizaciones...{bcolors.ENDC}")
        endpoint = self.url + "api/notifications/list"
        data = self.sReq.get(endpoint)
        info = data.json()
        self.sonar.organizations = info["organizations"]
        print(f"{bcolors.WARNING}[+] >>> Un total de {len(self.sonar.organizations)} organizaciones...{bcolors.ENDC}")

    # Lista los componentes
    def getComponents(self):
        print(f"{bcolors.OKGREEN}[+] Enumerando los componentes de codigo ...{bcolors.ENDC}")
        endpoint = self.url + "api/components/search"
        for org in self.sonar.organizations:
            params = "&qualifiers=FIL&organization={}".format(org["key"])
            data = self.sReq.get(endpoint + "?" + params[1:])
            info = data.json()
            self.sonar.components += self._paging(info, endpoint, params)
        print(f"{bcolors.WARNING}[+] >>> Un total de {len(self.sonar.components)} componentes de codigo...{bcolors.ENDC}")
    
    def _paging(self, data, url, params=""):
        # crear el paging _ extraer los demas datos
        key = list(data.keys())
        superior = 1
        page = 1 
        info = []
        if (len(key) == 2 and ("paging" in key)):
            key.remove("paging")
            key = key[0]
            superior = math.ceil(data["paging"]["total"]/500)
            
            for x in range(page, superior+1):
                print(url+"?p={}&ps=500".format(x)+params)
                tmp = self.sReq.get(url+"?p={}&ps=500".format(x)+params)
                tmp2 = tmp.json()
                info += tmp2[key]
            
            return info
        return data
        