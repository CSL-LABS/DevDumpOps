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
    PROJECTS_SEARCH = f"{bc.OKGREEN}[+] Total proyectos enumerados: {bc.ENDC}"
    PROJECTS_TOTAL = f"{bc.OKBLUE}[|] Total proyectos: {bc.ENDC}"
    CURRENT_USER = f"{bc.OKGREEN}[+] Usuario actual: {bc.ENDC}"
    USERS_TOKEN_SEARCH = f"{bc.OKBLUE}[|] Tokens creados por el usuario: {bc.ENDC}"
    WEBHOOKS_SEARCH = f"{bc.OKGREEN}[+] Buscando WebHooks de Proyectos: {bc.ENDC}"

    SETTINGS_OPT = f"{bc.OKGREEN}[+] Configuracion: {bc.ENDC}"
    SETTINGS_ERROR = f"{bc.FAIL}[-] No fue posible enumerar la configuracion ...{bc.ENDC}" 

    DUMP = f"{bc.OKGREEN}[+] Proceso de extraccion de informacion: OK{bc.ENDC}"
    DUMP_COMPONENTS = f"{bc.OKGREEN}[+] Extrayendo los componentes por organizacion: {bc.ENDC}"
    DUMP_COMPONENTS_TOTAL = f"{bc.OKBLUE}[|] Componentes enumerados: {bc.ENDC}"
    DUMP_COMPONENTS_ERROR = f"{bc.FAIL}[-] No fue posible enumerar los componentes de la organizacion: {bc.ENDC}"
    DUMP_SOURCE_RAW = f"{bc.OKGREEN}[+] Extrayendo el codigo fuente: {bc.ENDC}"

    def ONE_SETTING(componente, value):
        print(f"{bc.OKBLUE}[|] {componente}:{bc.ENDC} {value}")

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
    
    def SHOW_PROJECT(x, org, total):
        num = f"{bc.OKGREEN}{x}{bc.OKBLUE}"
        print(f"{bc.OKBLUE}[|] {num}: {org} -> {total} {bc.ENDC}")