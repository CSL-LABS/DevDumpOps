
class Dump():
    
    def __init__(self, url, request, path, dump):
        self.path = path + "/dump/"
        self.url = url
        self.dump = dump

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