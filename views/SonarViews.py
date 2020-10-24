from utils.Colors import Colors

# paleta de colores
bcolors = Colors()

class SonarViews():
    WS_VISIBILITY_OK = f"{bcolors.OKGREEN}[+] Acceso al WEB API: OK{bcolors.ENDC}"
    WS_VISIBILITY_ERROR = f"{bcolors.FAIL}[-] Acceso al WEB API: SIN PERMISOS{bcolors.ENDC}"
    SYS_ERROR = f"{bcolors.FAIL}[-] Sin version del servidor... {bcolors.ENDC}"
    USERS_SEARCH_ERROR = f"{bcolors.FAIL}[-] No fue posible enumerar los usuarios... {bcolors.ENDC}"
    USERS_SEARCH_COUNT = f"{bcolors.OKGREEN}[+] Total de usuarios enumerados: {bcolors.ENDC}"
    
    ORG_SEARCH = f"{bcolors.OKGREEN}[+] Organizaciones globales enumeradas: {bcolors.ENDC}"
    ORG_SEARCH_ERROR = f"{bcolors.FAIL}[-] No fue posible enumerar las organizaciones publicas ...{bcolors.ENDC}"
    ORG_SEARCH_MEMBER = f"{bcolors.OKGREEN}[+] Organizaciones a las que pertence la cuenta: {bcolors.ENDC}"
    ORG_SEARCH_MEMBER_ERROR = f"{bcolors.FAIL}[-] No fue posible enumerar las organizaciones de la cuenta ...{bcolors.ENDC}"
    DUMP_SAVE = f"{bcolors.OKBLUE}[|] Datos almacenados en: {bcolors.ENDC}"

    def TOP_LIST(jsonList, opt, top=10):
        if (len(jsonList)<10):
            top = len(jsonList)

        for x in range(0, top):
            objIter = jsonList[x]
            if(opt == "orgs"): 
                if(objIter.get("actions") != None):
                    action = objIter['actions']
                    print(f"{bcolors.OKBLUE}[|] {x}: {objIter['key']} -> {objIter['name']} {action}{bcolors.ENDC}")
            elif(opt == "users"):
                print(f"{bcolors.OKBLUE}[|] {x}: {objIter['login']} -> {objIter['name']} {bcolors.ENDC}")

    def SYS_VERSION(data):
        return f"{bcolors.OKBLUE}[|] Version SonarQube: {data['version']} \n[|] ID Server: {data['id']} \n[|] Status: {data['status']} {bcolors.ENDC}"
    