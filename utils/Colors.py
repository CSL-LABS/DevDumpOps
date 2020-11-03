import colorama

# Referencia: 
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-python

class Colors():
    colorama.init()
    # TODO: agregar mas colores 
    # Referencia: https://pypi.org/project/colorama/ 
    HEADER = '\033[47m'
    INPUT = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'