# Web API - SonarQube
# https://sonarcloud.io/web_api/

import requests
import base64
from model.Sonar import Sonar
from utils.Utils import Utils
from controller.SonarQube.Recon import Recon
from controller.SonarQube.Dump import Dump
from controller.SonarQube.BruteForce import BruteForce
from controller.SonarQube.BackDoor import BackDoor

class SonarController():
    def __init__(self, input):
        self.input = input
        self.sonar = Sonar(input.url)
        self.sReq = requests.Session()
        self.isAuthenticated = self._auth()
        
    def enumeration(self):
        enum = Recon(self.input.url[0], self.sReq, self.input.output, self.input.dump)
        self.sonar.users += enum.getUsers()

        if(self.isAuthenticated):
            enum.getUserToken()
            if(self.input.dump == "member"):
                self.sonar.organizationsMember = enum.getOrganizationsMember()
                self.sonar.authors += enum.getAuthors(self.sonar.organizationsMember)
                self.sonar.projects = enum.getProjects(self.sonar.organizationsMember)
            else:
                self.sonar.organizationsPublic = enum.getOrganizationsPublic()
                self.sonar.authors += enum.getAuthors(self.sonar.organizationsPublic)
                self.sonar.projects = enum.getProjects(self.sonar.organizationsPublic)
            self.sonar.webhooks = enum.getWebHooks(self.sonar.projects)
        else: 
            self.sonar.organizationsPublic = enum.getOrganizationsPublic()
            self.sonar.projects = enum.getProjects(self.sonar.organizationsPublic)
    
    def dumpInformation(self):
        i = 1
        dumpInfo = Dump(self.input.url[0], self.sReq, self.input.output)
        self.sonar.components += dumpInfo.getComponents(self.sonar.projects)

        for comp in self.sonar.components:
            dumpInfo.getSourceRaw(comp)
            Utils().printProgressBar(i, len(self.sonar.components))
            i += 1
        print("[+] SONAR DUMP: COMPLETED")
    
    def bfSonar(self):
        attack = BruteForce(self.input.url[0], self.sReq)
        attack.bruteForce()
        print("[+] SONAR BRUTEFORCE: COMPLETED")
    
    def backdoor(self):
        attack = BackDoor(self.input.url[0], self.sReq)
        #print("[+] SONAR BACKDOOR: COMPLETED")

    def _auth(self):
        auth = ""
        if(self.input.username != None and self.input.password != None):
            auth = self.input.username + ":" + self.input.password
        elif(self.input.token != None):
            auth = self.input.token + ":"
        
        if(auth):
            token = base64.b64encode(auth.encode("ascii")).decode("ascii")
            self.sReq.headers.update({"Authorization": "Basic " + token})
            return True
        return False
        