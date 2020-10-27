import math

class Utils():
    def __init__(self):
        pass

    def paging(data, url, sReq, params=""): # TODO: mejorar esta funcion para que sea legible
        # crear el paging _ extraer los demas datos
        key = list(data.keys())
        superior = 1
        page = 1 
        info = []
        if (len(key) == 2 and ("paging" in key)):
            key.remove("paging")
            key = key[0]
            superior = math.ceil(data["paging"]["total"]/500)
            for x in range(page, superior + 1):
                tmp = sReq.get(url + "?p={}&ps=500".format(x) + params)
                tmp2 = tmp.json()
                info += tmp2[key]
            
            return info
        return data