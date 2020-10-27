from views.SonarViews import SonarViews as sViews
from controller.SonarQube.Utils import Utils

class Recon():
    
    def __init__(self, url, request, path, dump):
        self.path = path + "/enumeration/"
        self.url = url
        self.dump = dump
        self.request = request
        self.isVisibilityWs()
        self.getVersion()

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
    
    def getOrganizations(self):
        endpoint = self.url + "api/organizations/search"
        reqPublic = self.request.get(endpoint)
        result = {}

        if(reqPublic.status_code == 200):
            data = reqPublic.json()
            print(sViews.ORG_SEARCH, data["paging"]["total"])

            if(self._validateQuantity(data["paging"]["total"])):
                orgPublic = Utils.paging(data, endpoint, self.request)
                sViews.TOP_LIST(orgPublic, "orgs") # vista top organizaciones publicas
                self._saveData(orgPublic, "orgs")
                result["orgPublic"] = orgPublic
            
            if(self.dump != None): # token o password para member
                reqMember = self.request.get(endpoint + "?member=true")
                if(reqMember.status_code == 200):
                    dataMember = reqMember.json()
                    orgMember = Utils.paging(dataMember, endpoint, self.request, "&member=true")
                    result["orgMember"] = orgMember

                    print(sViews.ORG_SEARCH_MEMBER, len(orgMember))
                    sViews.TOP_LIST(orgMember, "orgs") # vista top organizaciones miembro
                    self._saveData(orgMember, "orgsMember")
                    result["authors"] = self.getAuthors(orgMember)
                else: 
                    print(sViews.ORG_SEARCH_MEMBER_ERROR)
        else: 
            print(sViews.ORG_SEARCH_ERROR)
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
        result = []
        #print(orgs)
        for org in orgs:
            endpoint = self.url + "api/projects/search"
            getParam = "organization=" + org["key"]
            dataProject = self.request.get(endpoint + "?" + getParam)

            if(dataProject.status_code == 200):
                info = dataProject.json()
                projects = Utils.paging(info, endpoint, self.request, params="&"+getParam)
                result += projects
        #TODO: save projects
        #TODO: views projects
        return result

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
        opciones = {
            "users": ["users.txt", "LOGIN:NAME\n"],
            "orgs": ["orgs_public.txt", "ORGANIZATION:NAME\n"],
            "orgsMember" : ["orgs_member.txt", "ORGANIZATION:NAME:ADMIN:DELETE:PROVISION\n"],
            "authors": ["authors.txt", "AUTHORS\n"]
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
            elif(opt == "authors"):
                sline = "\nORGANIZATION: " + dataIter + "\n"
                for x in data[dataIter]:
                    sline += f"{x}\n"
            f.write(sline)
        print(sViews.DUMP_SAVE, filename)
        f.close()