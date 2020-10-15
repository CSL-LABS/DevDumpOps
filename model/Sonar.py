
class Sonar():
    def __init__(self, url, authorization):
        self.url = url 
        self.authorization = authorization

        self.authentication = {}
        self.badges = {}
        self.ce = {}
        self.cnesreport = {}
        self.components = []
        self.duplication = {}
        self.favorites = {}
        self.issues = {}
        self.languages = {}
        #licensecheck/licenses
        self.measures = {}
        self.metrics = {}
        self.new_code_periods = {}
        self.notifications = {}
        self.organizations = []
        self.permission = {}
        self.plugins = {}
        self.project_analyses = {}
        self.project_badges = {}
        self.project_branches = {}
        self.project_links = {}
        self.project_pull_requests = {}
        self.project_tags = {}
        self.projects = {}
        self.qualitygates = {}
        self.qualityprofiles = {}
        self.rules = {}
        self.server = ""
        self.settings = {}
        self.sources = {}
        self.system = {}
        self.user_groups = {}
        self.users_tokens = {}
        self.users = []
        self.webhooks = {}
        self.webservices = {}