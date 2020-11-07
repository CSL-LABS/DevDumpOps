import math
from utils.Utils import Utils as ut
from views.SonarViews import SonarViews as sViews

class Utils():
    def __init__(self):
        pass

    def paging(data, url, sReq, params="", progress=False): # TODO: mejorar esta funcion para que sea legible
        # crear el paging _ extraer los demas datos
        key = list(data.keys())
        superior = 1
        page = 1 
        info = []
        if ("paging" in key):
            key.remove("paging")
            if(len(key) >= 2):
                key = "components"
            else:
                key = key[0]
            superior = math.ceil(data["paging"]["total"]/500)
            for x in range(page, superior + 1):
                tmp = sReq.get(url + "?p={}&ps=500".format(x) + params)
                tmp2 = tmp.json()
                if(tmp.status_code == 200):
                    info += tmp2[key]
                    if(progress):
                        ut().printProgressBar(x, superior)
                else:
                    print("")
                    print(sViews.PAGING_ERROR)
                    break
            return info
        return data