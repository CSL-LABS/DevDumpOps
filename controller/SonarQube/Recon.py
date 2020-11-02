from views.SonarViews import SonarViews as sViews
from controller.SonarQube.Utils import Utils
from config.Config import Config

class Recon():
    
    def __init__(self, url, request, path, dump):
        self.path = path + "/enumeration/"
        self.url = url
        self.dump = dump
        self.request = request
        self.isVisibilityWs()
        self.getVersion()
        #self.getUserToken()
        self.getSettings()

    def isVisibilityWs(self):
        endpoint = self.url + "api/webservices/list" 
        ws = self.request.get(endpoint)
        if(ws.status_code == 200):
            print(sViews.WS_VISIBILITY_OK)
        else:
            print(sViews.WS_VISIBILITY_ERROR)
            exit(0)
        return True

    def getVersion(self):
        endpoint = self.url + "api/system/status"
        req = self.request.get(endpoint)
        if (req.status_code == 200):
            data = req.json()
            print(sViews.SYS_VERSION(data))
        else:
            print(sViews.SYS_ERROR)

    def getUsers(self):
        endpoint = self.url + "api/users/search"
        req = self.request.get(endpoint)
        users = []
        if (req.status_code == 200):
            data = req.json()
            print(sViews.USERS_SEARCH_COUNT + str(data["paging"]["total"])) # TODO: mejorar vista top user

            if(self._validateQuantity(data["paging"]["total"])):
                users = Utils.paging(data, endpoint, self.request)
                sViews.TOP_LIST(users, "users")
                self._saveData(users, "users")
        else: 
            print(sViews.USERS_SEARCH_ERROR)
        return users
    
    def getOrganizationsPublic(self):
        endpoint = self.url + "api/organizations/search"
        reqPublic = self.request.get(endpoint)
        result = []

        if(reqPublic.status_code == 200):
            data = reqPublic.json()
            print(sViews.ORG_SEARCH, data["paging"]["total"])

            if(self._validateQuantity(data["paging"]["total"])):
                orgPublic = Utils.paging(data, endpoint, self.request)
                sViews.TOP_LIST(orgPublic, "orgs") # vista top organizaciones publicas
                self._saveData(orgPublic, "orgs")
                result += orgPublic
        else: 
            print(sViews.ORG_SEARCH_ERROR)
        return result
    
    def getOrganizationsMember(self):
        endpoint = self.url + "api/organizations/search"
        reqMember = self.request.get(endpoint + "?member=true")
        result = []
        if(reqMember.status_code == 200):
            dataMember = reqMember.json()
            orgMember = Utils.paging(dataMember, endpoint, self.request, "&member=true")
            result += orgMember

            print(sViews.ORG_SEARCH_MEMBER, len(orgMember))
            sViews.TOP_LIST(orgMember, "orgs") # vista top organizaciones miembro
            self._saveData(orgMember, "orgsMember")
            #result["authors"] = self.getAuthors(orgMember)
        else: 
            print(sViews.ORG_SEARCH_MEMBER_ERROR)
        return result
    
    def getAuthors(self, orgs):
        print(sViews.AUTHORS_SEARCH)
        tmp = []
        authors = {}
        for org in orgs:
            endpoint = self.url + "api/issues/authors?organization=" + org["key"]
            authorReq = self.request.get(endpoint)
            dataAuthors = authorReq.json()

            authors[org["key"]] = dataAuthors["authors"]
            if(len(tmp)<10):    # show top
                sViews.AUTHORS_SEARCH_DUMP(org["key"], dataAuthors["authors"], t=len(tmp))
            tmp += dataAuthors["authors"]
        self._saveData(authors, "authors")
        return authors
    
    def getProjects(self, orgs):
        print(sViews.PROJECTS_SEARCH)
        result = []
        i = 0
        for org in orgs:
            endpoint = self.url + "api/projects/search"
            getParam = "organization=" + org["key"]
            dataProject = self.request.get(endpoint + "?" + getParam)

            if(dataProject.status_code == 200):
                info = dataProject.json()
                sViews.SHOW_PROJECT(i, org["key"], info["paging"]["total"])
                projects = Utils.paging(info, endpoint, self.request, params="&"+getParam)
                result += projects
            i+=1
        print(sViews.PROJECTS_TOTAL + str(len(result)))
        self._saveData(result, "projects")
        return result
    
    def getUserToken(self):
        endpoint = self.url + "api/user_tokens/search"
        dataReq = self.request.get(endpoint)
        if(dataReq.status_code == 200):
            info = dataReq.json()
            print(sViews.CURRENT_USER + info["login"])
            print(sViews.USERS_TOKEN_SEARCH + str(len(info["userTokens"])))
            self._saveData(info["userTokens"], "userTokens")
    
    def getWebHooks(self, projects):
        print(sViews.WEBHOOKS_SEARCH, len(projects))
        result = []
        for pj in projects: 
            endpoint = self.url + "api/webhooks/list?organization={}&project={}".format(pj["organization"], pj["key"])
            dataReq = self.request.get(endpoint)
            if(dataReq.status_code == 200):
                info = dataReq.json()
                if(info["webhooks"]):
                    result += info["webhooks"]
        if(result):
            self._saveData(result, "webHooks")
        return result
    
    def getSettings(self):
        endpoint = self.url + "api/settings/values"
        dataReq = self.request.get(endpoint)

        if(dataReq.status_code == 200):
            settings = dataReq.json()
            for opt in Config.SONARQUBE_API_SETTINGS:
                print(sViews.SETTINGS_OPT + opt)
                for key in settings["settings"]:
                    if(key["key"] in Config.SONARQUBE_API_SETTINGS[opt]):
                        sViews.ONE_SETTING(key["key"], key["value"])
        else: 
            print(sViews.SETTINGS_ERROR)

    def _validateQuantity(self, quantity):
        if(self.dump == "all"):
            return True
        if(quantity > 10000):
            print(sViews.QUANTITY_QUESTION, )
            opt = input()
            if(opt.lower() != "y"):
                return False
        return True
    
    def _saveData(self, data, opt):
        #TODO: mejorar esta funcion, es muy compleja de leer/seguir
        select = Config.SONARQUBE_FILE_SAVE_RECON[opt]

        filename = self.path + select[0]
        f = open(filename, "w")
        f.write(select[1])
        for dataIter in data:
            if(opt == "users"):
                sline = f"{dataIter['login']}:{dataIter['name']}\n"
            elif(opt == "orgs"):
                sline = f"{dataIter['key']}:{dataIter['name']}\n"
            elif(opt == "orgsMember"):
                action = dataIter['actions']
                sline = f"{dataIter['key']}:{dataIter['name']}:{action['admin']}:{action['delete']}:{action['provision']}\n"
            elif(opt == "authors"):
                sline = "\nORGANIZATION: " + dataIter + "\n"
                for x in data[dataIter]:
                    sline += f"{x}\n"
            elif(opt == "projects"):
                sline = f"{dataIter['organization']}:{dataIter['key']}:{dataIter['name']}\n"
            elif(opt == "userTokens"):
                sline = f"{dataIter['name']}:{dataIter['createdAt']}\n"
            elif(opt == "webHooks"):
                tmp = ""
                if(dataIter.get("secret") != None):
                    tmp = dataIter["secret"]
                sline = f"{dataIter['name']}:{dataIter['url']}:{tmp}\n"
            f.write(sline)
        print(sViews.DUMP_SAVE, filename)
        f.close()