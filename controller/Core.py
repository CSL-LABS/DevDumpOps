#!/usr/bin/env python
# encoding=utf-8
import base64
from controller.InputParser import InputParser
from controller.SonarController import SonarController

class Core():
    def __init__(self):
        self.input = InputParser().args

        if(self.input.sonarqube):
            self.sonarLogic()
        else:
            print("En construccion ;)")
            exit(0)
        print("[+] Thanks for using me ;)")
        #TODO: otros targets
    
    def sonarLogic(self):
        sonar = SonarController(self.input)
        if(self.input.backdoor):
            sonar.backdoor()
        elif(self.input.bruteforce):
            sonar.bfSonar()
        else:
            sonar.enumeration()

        if(self.input.dump != None): #TODO: agregar opciones del dump
            sonar.dumpInformation()