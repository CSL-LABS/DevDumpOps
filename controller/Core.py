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
        #TODO: otros targets
    
    def sonarLogic(self):
        sonar = SonarController(self.input)
        sonar.enumeration()
        if(self.input.dump != None): #TODO: agregar opciones del dump
            sonar.dumpInformation()