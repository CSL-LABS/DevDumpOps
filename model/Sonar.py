
class Sonar():
    def __init__(self, url):
        self.url = url

        self.authors = []
        self.components = []
        self.issues = {}
        self.notifications = {}
        self.organizationsPublic = []
        self.organizationsMember = []
        self.permission = {}
        self.plugins = {}
        self.projects = {}
        self.server = ""
        self.settings = {}
        self.sources = {}
        self.system = {}
        self.users_tokens = {}
        self.users = []
        self.webhooks = {}