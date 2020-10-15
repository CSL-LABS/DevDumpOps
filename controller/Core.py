#!/usr/bin/env python
# encoding=utf-8

from controller.InputParser import InputParser
from controller.SonarQube import SonarQube

class Core():
    def __init__(self):
        self.input = InputParser().args
        self.auth = self._auth()
        if(self.input.sonarqube):
            sonar = SonarQube(self.input.url[0], self.auth)
            sonar.dump(self.input.output + "/dump/")
    
    # logica username-password-token
    def _auth(self):
        auth = ""
        if(self.input.username != None and self.input.password != None):
            auth = self.input.username + ":" + self.input.password 
        elif(self.input.token != None):
            auth = self.input.token + ":"
        return auth