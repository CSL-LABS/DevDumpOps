import argparse
from utils.Colors import Colors
from utils.Utils import Utils

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
            help="Plataforma SonarQube")
        grupoExc_activos.add_argument("--jenkins",
            action="store_true",
            help="Plataforma Jenkins")
        grupoExc_activos.add_argument("--maven",
            action="store_true",
            help="Plataforma Maven")
        
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
            action="store_false",   # por defecto primero enumera
            help="Enumerar todos los recursos")
        gpActions.add_argument("--dump",
            action="store_true",
            help="Dumpear todos los recursos")

        # Parametros generales
        parser.add_argument("url", type=str,
            nargs=1,
            help="URL del servicio",
            metavar="[URL:PORT]")
        parser.add_argument("-u",
            dest="username",
            action="store",
            help="Usuario de conexion")
        parser.add_argument("-p",
            dest="password",
            action="store",
            help="Password de conexion")
        parser.add_argument("-t",
            dest="token",
            action="store",
            help="Token de conexion")
        parser.add_argument("--output",
            dest="output",
            action="store",
            default="results",
            help="Directorio de resultados")

        self.args = parser.parse_args()
        Utils().createdFolders(self.args.output)
        self.verify_conection()
        print(self.args)
        print("test")
            
    def verify_conection(self):
        if(not Utils().testVisibility(self.args.url[0])):
            exit(0)
    
    def showBanner(self):
        # Referencia: 
        # https://manytools.org/hacker-tools/ascii-banner/
        # Tinker-Toy

        bcolors = Colors()
        banner = f"""{bcolors.WARNING}o-o             {bcolors.OKBLUE}o-o                    {bcolors.OKGREEN}o-o           
{bcolors.WARNING}|  \            {bcolors.OKBLUE}|  \                  {bcolors.OKGREEN}o   o          
{bcolors.WARNING}|   O o-o o   o {bcolors.OKBLUE}|   O o  o o-O-o o-o  {bcolors.OKGREEN}|   | o-o  o-o 
{bcolors.WARNING}|  /  |-'  \ /  {bcolors.OKBLUE}|  /  |  | | | | |  | {bcolors.OKGREEN}o   o |  |  \  
{bcolors.WARNING}o-o   o-o   o   {bcolors.OKBLUE}o-o   o--o o o o O-o  {bcolors.OKGREEN} o-o  O-o  o-o 
   @csl-labs /|\ csl@csl.com.co  {bcolors.OKBLUE}|          {bcolors.OKGREEN}|        
                                 {bcolors.OKBLUE}o          {bcolors.OKGREEN}o        
 
{bcolors.ENDC}"""
        print(banner)