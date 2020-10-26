#!/usr/bin/env python
# encoding=utf-8
import base64
from controller.InputParser import InputParser
from controller.SonarController import SonarController

class Core():
    def __init__(self):
        self.input = InputParser().args
        self.auth = self._auth()
        if(self.input.sonarqube):
            sonar = SonarController(self.input.url[0], self.auth, self.input.output)
            print("test")
            #sonar.dump(self.input.output + "/dump/")
    
    # logica username-password-token
    def _auth(self):
        auth = ""
        flag = True
        if(self.input.username != None and self.input.password != None):
            auth = self.input.username + ":" + self.input.password 
        elif(self.input.token != None):
            auth = self.input.token + ":"
        else:
            flag = False
        authorization = base64.b64encode(auth.encode("ascii")).decode("ascii")
        return authorization, flag