class Config(): 
    SONARQUBE_LIST_TO = 10 #TODO: integrar con las funciones de LIST TOP
    SONARQUBE_FILE_SAVE_RECON = {
            "users": ["users.txt", "LOGIN:NAME\n"],
            "orgs": ["orgs_public.txt", "ORGANIZATION:NAME\n"],
            "orgsMember" : ["orgs_member.txt", "ORGANIZATION:NAME:ADMIN:DELETE:PROVISION\n"],
            "authors": ["authors.txt", "AUTHORS\n"],
            "projects": ["projects.txt", "ORGANIZATION:PROJECT:NAME\n"],
            "userTokens": ["userTokens.txt", "NAME-TOKENS:CREATED-AT\n"],
            "webHooks": ["webHooks.txt", "NAME:URL:SECRET\n"]
    }
    SONARQUBE_FILE_SAVE_DUMP = {
            "components": ["components.txt", "ORGANIZATION:PROJECT:PATH\n"]
    } 
    SONARQUBE_API_SETTINGS = {
            "EMAIL": ["email.fromName", "email.from", "email.prefix", "email.smtp_port.secured", 
                    "email.smtp_host.secured", "email.smtp_password.secured", "email.smtp_username.secured"],
            "SVN": ["sonar.svn.username", "sonar.svn.password.secured", "sonar.svn.privateKeyPath",
                    "sonar.svn.passphrase.secured"],
            "GITLAB": ["sonar.auth.gitlab.enabled", "sonar.auth.gitlab.groupsSync", "sonar.auth.gitlab.allowUsersToSignUp", 
                    "sonar.auth.gitlab.url", "sonar.auth.gitlab.applicationId", "sonar.auth.gitlab.secret"],
            "GITHUB": ["sonar.auth.github.enabled", "sonar.auth.github.apiUrl", "sonar.auth.github.webUrl",
                    "sonar.auth.github.groupsSync", "sonar.auth.github.allowUsersToSignUp", "sonar.auth.github.clientId.secured",
                    "sonar.auth.github.clientSecret.secured"]}

