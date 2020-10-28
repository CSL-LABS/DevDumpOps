# Web API - SonarQube
# https://sonarcloud.io/web_api/

import requests
import base64
from model.Sonar import Sonar
from controller.SonarQube.Recon import Recon
from utils.Colors import Colors

# paleta de colores
bcolors = Colors()

class SonarController():
    def __init__(self, input):
        self.input = input
        self.sonar = Sonar(input.url)
        self.sReq = requests.Session()
        self._auth()
        
    def enumeration(self):
        #logica - enumeracion
        enum = Recon(self.input.url[0], self.sReq, self.input.output, self.input.dump)
        self.sonar.users += enum.getUsers()
        self.sonar.organizations = enum.getOrganizations()
        
        if(self.sonar.organizations.get("orgMember") != None):
            self.sonar.projects = enum.getProjects(self.sonar.organizations["orgMember"])
        else:
            self.sonar.projects = enum.getProjects(self.sonar.organizations["orgPublic"])
        
        self.sonar.webhooks = enum.getWebHooks(self.sonar.projects)
    
    def _auth(self):
        auth = ""
        if(self.input.username != None and self.input.password != None):
            auth = self.input.username + ":" + self.input.password
        elif(self.input.token != None):
            auth = self.input.token + ":"
        
        if(auth):
            token = base64.b64encode(auth.encode("ascii")).decode("ascii")
            self.sReq.headers.update({"Authorization": "Basic " + token})
        