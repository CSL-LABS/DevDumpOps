#!/usr/bin/env python
# encoding=utf-8

from controller.InputParser import InputParser

class Core():
    def __init__(self):
        self.input = InputParser().args