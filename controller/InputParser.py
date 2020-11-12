import argparse
from utils.Colors import Colors
from utils.Utils import Utils

# paleta de colores
bcolors = Colors()

class InputParser():
    def __init__(self): # Generador ArgParse
        #TODO: configParser - http://46.101.4.154/Art%C3%ADculos%20t%C3%A9cnicos/Python/ConfigParser.pdf 
        self.showBanner()

        #devdumpops --sonarqube --enumeration -u [user] -p [password] -token [token] --output [DIR] [HOST:PORT]
        #devdumpops --sonarqube --dump -u [user] -p [password] -token [token] --output [DIR] [HOST:PORT]

        parser = argparse.ArgumentParser(description="DevDumpOps",
            epilog="Ejemplos de uso: -*- asd bc de de") #TODO: agregar ejemplo de uso
        
        #TODO: agregar demas opciones JIRA, GRANDLE
        # Opciones TARGETS
        gpTarget = parser.add_argument_group(title="Target's")
        grupoExc_activos = gpTarget.add_mutually_exclusive_group()
        grupoExc_activos.add_argument("--sonarqube", 
            action="store_true",
            default=True,
            help="SonarQube platform")
        #grupoExc_activos.add_argument("--jenkins",
        #    action="store_true",
        #    help="Plataforma Jenkins")
        #grupoExc_activos.add_argument("--maven",
        #    action="store_true",
        #    help="Plataforma Maven")
        
        # Opciones Configuracion Proxy
        gpProxy = parser.add_argument_group(title="Proxy - Optional")
        gpProxy.add_argument("--phost",
            action="store",
            help="Host PROXY")
        gpProxy.add_argument("--pport",
            action="store",
            help="Port PROXY")
        gpProxy.add_argument("--puser",
            action="store",
            help="Username PROXY")
        gpProxy.add_argument("--ppwd",
            action="store",
            help="Password PROXY")

        # Opciones de las acciones
        gpActions = parser.add_argument_group(title="Actions").add_mutually_exclusive_group()
        gpActions.add_argument("--enumeration", 
            action="store_true",
            default=True,  # por defecto primero enumera
            help="List all resources")
        gpActions.add_argument("--dump",
            action="store",
            choices=("all","member"),
            help="Dump all resources")
        gpActions.add_argument("--bruteforce",
            action="store_true",
            help="Brute Force Attack")
        gpActions.add_argument("--backdoor",
            action="store_true",
            help="Persistence techniques")

        # Parametros generales
        parser.add_argument("url",
            type=str,
            nargs=1,
            help="Service url",
            metavar="[URL:PORT]")
        parser.add_argument("-u",
            dest="username",
            action="store",
            help="Connection user")
        parser.add_argument("-p",
            dest="password",
            action="store",
            help="Connection password")
        parser.add_argument("-t", 
            dest="token",
            action="store",
            help="Connection Token")
        parser.add_argument("--output",
            dest="output",
            action="store",
            default="results",
            help="Results directory")

        self.args = parser.parse_args()
        self._validateMember()
        self.strucURL()
        self._lastChar()
        self.verify_conection()
        Utils().createdFolders(self.args.output)

        #print(self.args)
        #print("test")
    
    def _lastChar(self):
        if(self.args.url[0][-1] != "/"):
            self.args.url[0] += "/"
            
    def verify_conection(self):
        proxy = self.armerProxy()
        if(not Utils().testVisibility(self.args.url[0], proxy)):
            exit(0)
        print(f"{bcolors.OKGREEN}[+] VISIBILITY: {bcolors.ENDC}OK")
    
    def armerProxy(self):
        if(self.args.phost != None):
            if self.args.puser != None:
                proxy_auth = self.args.puser + ":" + self.args.ppwd
                proxies = {
                    "https": "https://{}@{}:{}/".format(proxy_auth, self.args.phost, self.args.pport),
                    "http": "http://{}@{}:{}/".format(proxy_auth, self.args.phost, self.args.pport)
                }
            else: 
                proxies = {
                    "https": "https://{}:{}/".format(self.args.phost, self.args.pport),
                    "http": "http://{}:{}/".format(self.args.phost, self.args.pport)
                }
        else: 
            proxies = {}
        return proxies
    
    def _validateMember(self):
        if(self.args.dump == "member"):
            if(self.args.username == None and self.args.token == None):
                print(f"{bcolors.FAIL}[-] Dump - member: Requires credentials{bcolors.ENDC}")
                exit(0)

    def strucURL(self):
        url = self.args.url[0]
        if(not (url.startswith("http://") or url.startswith("https://"))):
            self.args.url = ["http://" + url]

    def showBanner(self):
        # Referencia: 
        # https://manytools.org/hacker-tools/ascii-banner/
        # Tinker-Toy

        banner = f"""{bcolors.WARNING}o-o             {bcolors.OKBLUE}o-o                    {bcolors.OKGREEN}o-o           
{bcolors.WARNING}|  \            {bcolors.OKBLUE}|  \                  {bcolors.OKGREEN}o   o          
{bcolors.WARNING}|   O o-o o   o {bcolors.OKBLUE}|   O o  o o-O-o o-o  {bcolors.OKGREEN}|   | o-o  o-o 
{bcolors.WARNING}|  /  |-'  \ /  {bcolors.OKBLUE}|  /  |  | | | | |  | {bcolors.OKGREEN}o   o |  |  \  
{bcolors.WARNING}o-o   o-o   o   {bcolors.OKBLUE}o-o   o--o o o o O-o  {bcolors.OKGREEN} o-o  O-o  o-o 
   {bcolors.FAIL}@csl-labs /|\ csl@csl.com.co  {bcolors.OKBLUE}|          {bcolors.OKGREEN}|        
                                 {bcolors.OKBLUE}o          {bcolors.OKGREEN}o        
{bcolors.ENDC}"""
        print(banner)