from utils.Colors import Colors

# paleta de colores
bc = Colors()

class SonarViews():
    WS_VISIBILITY_OK = f"{bc.OKGREEN}[+] Acceso al WEB API: OK{bc.ENDC}"
    WS_VISIBILITY_ERROR = f"{bc.FAIL}[-] Acceso al WEB API: SIN PERMISOS{bc.ENDC}"
    SYS_ERROR = f"{bc.FAIL}[-] Sin version del servidor... {bc.ENDC}"
    USERS_SEARCH_ERROR = f"{bc.FAIL}[-] No fue posible enumerar los usuarios... {bc.ENDC}"
    USERS_SEARCH_COUNT = f"{bc.OKGREEN}[+] Total de usuarios enumerados: {bc.ENDC}"
    
    ORG_SEARCH = f"{bc.OKGREEN}[+] Total de organizaciones publicas: {bc.ENDC}"
    ORG_SEARCH_ERROR = f"{bc.FAIL}[-] No fue posible enumerar las organizaciones publicas ...{bc.ENDC}"
    ORG_SEARCH_MEMBER = f"{bc.OKGREEN}[+] TOP Organizaciones asociadas: {bc.ENDC}"
    ORG_SEARCH_MEMBER_ERROR = f"{bc.FAIL}[-] No fue posible enumerar las organizaciones asociadas ...{bc.ENDC}"
    DUMP_SAVE = f"{bc.OKBLUE}[\] {bc.HEADER}Datos almacenados en: {bc.ENDC}"

    AUTHORS_SEARCH = f"{bc.OKGREEN}[+] TOP autores de ISSUES: {bc.ENDC}"
    QUANTITY_QUESTION = f"{bc.INPUT}[¿] Quieres extraer todos los registros?{bc.ENDC} Y/n: "

    def TOP_LIST(jsonList, opt, top=10):
        if (len(jsonList)<10):
            top = len(jsonList)

        for x in range(0, top):
            objIter = jsonList[x]
            num = f"{bc.OKGREEN}{x}{bc.OKBLUE}"
            if(opt == "orgs"): 
                if(objIter.get("actions") != None):
                    action = objIter['actions']
                    print(f"{bc.OKBLUE}[|] {num}: {objIter['key']} -> {objIter['name']} -> {action}{bc.ENDC}")
            elif(opt == "users"):
                print(f"{bc.OKBLUE}[|] {num}: {objIter['login']} -> {objIter['name']} {bc.ENDC}")

    def SYS_VERSION(data):
        return f"{bc.OKBLUE}[|] Version SonarQube: {data['version']} \n[|] ID Server: {data['id']} \n[\] Status: {data['status']} {bc.ENDC}"
    
    def AUTHORS_SEARCH_DUMP(org, data, top=10, t=0):
        for x in data:
            num = f"{bc.OKGREEN}{t}{bc.OKBLUE}"
            if(t<top):
                print(f"{bc.OKBLUE}[|] {num}: {x} {bc.ENDC}")
            t += 1