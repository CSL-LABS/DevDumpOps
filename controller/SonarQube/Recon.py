from views.SonarViews import SonarViews as sViews
from controller.SonarQube.Utils import Utils

class Recon():
    
    def __init__(self, url, request, path):
        self.path = path + "/enumeration/"
        self.url = url
        self.request = request
        if(self.isVisibilityWs()):
            self.getVersion()
            self.getUsers()
            self.getOrganizations()

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
        if (req.status_code == 200):
            data = req.json()
            users = Utils.paging(data, endpoint, self.request)

            print(sViews.USERS_SEARCH_COUNT + str(data["paging"]["total"])) # vista top users
            sViews.TOP_LIST(users, "users")
            self._saveData(users, "users")
        else: 
            print(sViews.USERS_SEARCH_ERROR)
    
    def getOrganizations(self):
        endpoint = self.url + "api/organizations/search"
        reqPublic = self.request.get(endpoint)

        if(reqPublic.status_code == 200):
            data = reqPublic.json()
            orgPublic = Utils.paging(data, endpoint, self.request)

            print(sViews.ORG_SEARCH, len(orgPublic))
            sViews.TOP_LIST(orgPublic, "orgs") # vista top organizaciones publicas
            self._saveData(orgPublic, "orgs")

            reqMember = self.request.get(endpoint + "?member=true")
            if(reqMember.status_code == 200):
                dataMember = reqMember.json()
                orgMember = Utils.paging(dataMember, endpoint, self.request, "&member=true")

                print(sViews.ORG_SEARCH_MEMBER, len(orgMember))
                sViews.TOP_LIST(orgMember, "orgs") # vista top organizaciones miembro
                self._saveData(orgPublic, "orgsMember")
            else: 
                print(sViews.ORG_SEARCH_MEMBER_ERROR)
        else: 
            print(sViews.ORG_SEARCH_ERROR)
    
    def _saveData(self, data, opt):
        opciones = {
            "users": ["users.txt", "LOGIN:NAME\n"],
            "orgs": ["orgs_public.txt", "ORGANIZATION:NAME\n"],
            "orgsMember" : ["orgs_member.txt", "ORGANIZATION:NAME:ADMIN:DELETE:PROVISION\n"]
        }
        select = opciones[opt]

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
            f.write(sline)
        print(sViews.DUMP_SAVE, filename)
        f.close()
    
    def _saveUsers(self, users):
        filename = self.path + "users.txt"
        archivo = open(filename, "w")
        archivo.write("Login:Name\n")
        for user in users:
            tmp = f"{user['login']}:{user['name']}\n"
            archivo.write(tmp)
        archivo.close()
        print(sViews.USERS_SEARCH_SAVE + filename)