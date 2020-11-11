from utils.Colors import Colors

# paleta de colores
bc = Colors()

class SonarViews():
    WS_VISIBILITY_OK = f"{bc.OKGREEN}[+] WEB API: {bc.ENDC} OK"
    WS_VISIBILITY_ERROR = f"{bc.FAIL}[-] WEB API: NOT AUTHORIZED{bc.ENDC}"
    SYS_ERROR = f"{bc.FAIL}[-] SERVER INFO: NOT AUTHORIZED{bc.ENDC}"
    USERS_SEARCH_ERROR = f"{bc.FAIL}[-] USER ENUMERATION: NOT AUTHORIZED {bc.ENDC}"
    USERS_SEARCH_COUNT = f"{bc.OKGREEN}[+] USER ENUMERATION: {bc.ENDC}"
    
    ORG_SEARCH = f"{bc.OKGREEN}[+] ORGS (PUBLIC) ENUMERATION: {bc.ENDC}"    #TODO: ¿Falta top, orgs public?
    ORG_SEARCH_ERROR = f"{bc.FAIL}[-] ORGS (PUBLIC) ENUMERATION: NOT AUTHORIZED{bc.ENDC}"
    ORG_SEARCH_MEMBER = f"{bc.OKGREEN}[+] TOP - ORGS (MEMBER) ENUMERATION: {bc.ENDC}"
    ORG_SEARCH_MEMBER_ERROR = f"{bc.FAIL}[-] ORGS (MEMBER) ENUMERATION: NOT AUTHORIZED {bc.ENDC}"
    DUMP_SAVE = f"{bc.OKBLUE}  [\] {bc.HEADER}FILE PATH:{bc.ENDC}"

    QUANTITY_BEGIN = f"{bc.INPUT}"
    QUANTITY_QUESTION = "  [¿] Extract? Y/n: "
    QUANTITY_END = f"{bc.ENDC}"

    AUTHORS_SEARCH = f"{bc.OKGREEN}[+] TOP - ISSUES AUTHORS: {bc.ENDC}"
    PROJECTS_SEARCH = f"{bc.OKGREEN}[+] PROJECTS ENUMERATION{bc.ENDC}"
    PROJECTS_TOTAL = f"{bc.OKBLUE}  [|] Total projects: {bc.ENDC}"
    CURRENT_USER = f"{bc.OKGREEN}[+] CURRENT USER: {bc.ENDC}"
    USERS_TOKEN_SEARCH = f"{bc.OKBLUE}  [|] Tokens of user: {bc.ENDC}"
    WEBHOOKS_SEARCH = f"{bc.OKGREEN}[+] WEBHOOKS ENUMERATION: {bc.ENDC}"

    SETTINGS_OPT = f"{bc.OKGREEN}[+] SETTINGS: {bc.ENDC}"
    SETTINGS_ERROR = f"{bc.FAIL}[-] SETTINGS: NOT AUTHORIZED {bc.ENDC}" 

    DUMP = f"{bc.OKGREEN}[+] DUMP INFO: {bc.ENDC}"
    DUMP_COMPONENTS = f"{bc.OKBLUE}  [|] Component extraction: {bc.ENDC} OK"
    DUMP_COMPONENTS_TOTAL = f"{bc.OKBLUE}  [|] Component enumeration: {bc.ENDC}"
    DUMP_COMPONENTS_ERROR = f"{bc.FAIL}  [-] Component enumeration: NOT AUTHORIZED | {bc.ENDC}"
    DUMP_SOURCE_RAW = f"{bc.OKGREEN}[+] DOWNLOAD SOURCE CODE: {bc.ENDC}"

    SONAR_COMPLETED = f"{bc.OKGREEN}[+] SONAR DUMP: COMPLETED \n  {bc.ENDC}"

    PAGING_ERROR = f"{bc.FAIL}  [-] 10.000 records passed{bc.ENDC}"

    BRUTEFORCE_START = f"{bc.OKGREEN}[+] BRUTEFORCE START: {bc.ENDC}"
    BRUTEFORCE_OK = f"{bc.WARNING}  [|] Password Found: {bc.ENDC}"
    BRUTEFORCE_END = f"{bc.OKBLUE}  [\] BruteForce End{bc.ENDC}"
    BRUTEFORCE_ERROR = f"{bc.FAIL}  [-] Password NOT Found {bc.ENDC}"
    BRUTEFORCE_DICT_ERROR = f"{bc.FAIL}  [-] File Dict NOT Found {bc.ENDC}"

    BACKDOOR_START = f"{bc.OKGREEN}[+] BACKDOOR START: {bc.ENDC}"
    BACKDOOR_TOKEN_GEN = f"{bc.WARNING}  [|] Token Generated: {bc.ENDC}"
    BACKDOOR_CREATED_USER = f"{bc.WARNING}  [|] User created! {bc.ENDC}"
    BACKDOOR_PERMISSIONS_OK = f"{bc.WARNING}  [|] Add permission!:  {bc.ENDC}"
    BACKDOOR_PERMISSIONS_ERROR = f"{bc.FAIL}  [|] No privileges to add permissions: {bc.ENDC}"
    BACKDOOR_CHANGE_PWD_OK = f"{bc.WARNING}  [|] Password changed successfully! {bc.ENDC}"
    BACKDOOR_CHANGE_PWD_400 = f"{bc.FAIL}  [-] No privileges to change password {bc.ENDC}"
    BACKDOOR_MENU_ERROR = f"{bc.FAIL}  [-] Select a valid option {bc.ENDC}"
    BACKDOOR_ERROR_400 = f"{bc.FAIL}  [-] The Object already exists {bc.ENDC}"
    BACKDOOR_ERROR_401 = f"{bc.FAIL}  [-] Authentication is required {bc.ENDC}"
    BACKDOOR_ERROR_403 =  f"{bc.FAIL}  [-] Insufficient privileges {bc.ENDC}"
    BACKDOOR_ERROR = f"{bc.FAIL}  [-] Error params backdoor genereted {bc.ENDC}"
    BACKDOOR_END = f"{bc.OKBLUE}  [\] Backdoor End{bc.ENDC}"

    def ONE_SETTING(componente, value):
        print(f"{bc.OKBLUE}  [|] {componente}:{bc.ENDC} {value}")

    def TOP_LIST(jsonList, opt, top=10):
        g = f"{bc.OKGREEN}"
        b = f"{bc.OKBLUE}"
        if (len(jsonList)<10):
            top = len(jsonList)

        for x in range(0, top):
            objIter = jsonList[x]
            num = f"{bc.OKGREEN}{x+1}{bc.OKBLUE}"
            if(opt == "orgs"): 
                if(objIter.get("actions") != None):
                    tmp = str(objIter['actions']).replace("True","T").replace("False","F")
                    print(f"{bc.OKBLUE}  [|] {num}: {objIter['key']} {g}| Desc: {b}{objIter['name']} {g}| Act: {b}{tmp}{bc.ENDC}")
            elif(opt == "users"):
                print(f"{bc.OKBLUE}  [|] {num}: {objIter['login']} {g}| Name: {b}{objIter['name']} {bc.ENDC}")

    def SYS_VERSION(data):
        print(f"{bc.OKBLUE}  [|] Version SonarQube: {bc.ENDC} {data['version']}")
        print(f"{bc.OKBLUE}  [|] ID Server: {bc.ENDC} {data['id']}")
        print(f"{bc.OKBLUE}  [\] Status: {bc.ENDC} {data['status']}")
    
    def AUTHORS_SEARCH_DUMP(org, data, top=10, t=0):
        for x in data:
            num = f"{bc.OKGREEN}{t+1}{bc.OKBLUE}"
            if(t<top):
                print(f"{bc.OKBLUE}  [|] {num}: {x} {bc.ENDC}")
            t += 1
    
    def SHOW_PROJECT(x, org, total):
        g = f"{bc.OKGREEN}"
        b = f"{bc.OKBLUE}"
        if(x < 10):
            num = f"{bc.OKGREEN}{x+1}{bc.OKBLUE}"
            print(f"{bc.OKBLUE}  [|] {num}: {org} {g}| Total: {b}{total} {bc.ENDC}")
    
    def menuBackdoor():
        opts =  f"{bc.OKBLUE}  [|] Options Backdoor:{bc.ENDC}\n"
        opts += "    [1] Create New User\n"
        opts += "    [2] Generate New Token\n"
        opts += "    [3] Elevate Privileges\n"
        opts += "    [4] Change Password for User\n"
        opts += "    [0] Exit"
        print(opts)