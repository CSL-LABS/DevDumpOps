from views.SonarViews import SonarViews as sViews
from controller.SonarQube.Utils import Utils
from config.Config import Config
import os

class Dump():
    
    def __init__(self, url, request, path):
        self.path = path + "/dump/"
        self.url = url
        self.request = request
        print(sViews.DUMP)
    
    # Descarga codigo por key
    def getSourceRaw(self, component):
        # TODO: ¿los archivos antiguos?
        # ¿¿cada version sera un proyecto diferente?? 
        # o debo validar que no este sobreescribiendo archivos
        path = self._validatePath(component)
        path += "/" + component["name"]
        endpoint = self.url + "api/sources/raw?key="
        data = self.request.get(endpoint + component["key"])

        with open(path, "wb") as f:
            f.write(data.content)

    # Lista los componentes
    def getComponents(self, orgs):
        print(sViews.DUMP_COMPONENTS)
        endpoint = self.url + "api/components/search"
        result = []
        for org in orgs:
            params = "&qualifiers=FIL&organization={}".format(org["key"])
            data = self.request.get(endpoint + "?" + params[1:]) 
            if(data.status_code == 200):
                info = data.json()
                result += Utils.paging(info, endpoint, self.request, params)
            else:
                print(sViews.DUMP_COMPONENTS_ERROR + org["key"])
        print(sViews.DUMP_COMPONENTS_TOTAL, len(result))
        self._saveData(result, "components")
        print(sViews.DUMP_SOURCE_RAW, len(result), " files")
        return result
    
    def _validatePath(self, component):
        key = component["key"]
        tmpPath = (component["organization"] + "/" + key.replace(":","/")).split("/")
        tmpPath.pop()
        localPath = self.path + "/".join(tmpPath)
        if not os.path.exists(localPath):
            os.makedirs(localPath)
        return localPath
    
    def _saveData(self, data, opt):
        select = Config.SONARQUBE_FILE_SAVE_DUMP[opt]

        filename = self.path + select[0]
        f = open(filename, "w")
        f.write(select[1])
        for dataIter in data:
            if(opt == "components"):
                sline = f"{dataIter['organization']}:{dataIter['project']}:{dataIter['key']}\n"
            f.write(sline)
        print(sViews.DUMP_SAVE, filename)
        f.close()