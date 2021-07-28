from locust import HttpLocust, TaskSet, task, between
import random, string


class UserBehaviour(TaskSet):

  
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.start()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.stop()

    def stop(self):
        self.client.get("WebGoat")

    def start(self):
        self.client.get("WebGoat")
    
    @task
    def all(self):
        self.client.get("WebGoat/registration")
        self.client.post("WebGoat/register.mvc", {"agree":"agree", "username":"admin1", "password":"admin1", "matchingPassword":"admin1"})
        self.client.post("WebGoat/login", {"username":"admin1", "password":"admin1"})
        self.client.get("WebGoat/challenge/7/.git")
        self.client.get("WebGoat/challenge/8/vote/5")
        self.client.get("WebGoat/challenge/8/votes/")
        self.client.get("WebGoat/challenge/8/votes/average")
        self.client.get("WebGoat/clientSideFiltering/salaries")
        self.client.get("WebGoat/CrossSiteScripting/quiz")
        self.client.get("WebGoat/CrossSiteScriptingStored/stored-xss")
        self.client.get("WebGoat/csrf/review")
        self.client.get("WebGoat/JWT/votings")
        self.client.get("WebGoat/PasswordReset/reset/change-password")
        self.client.get("WebGoat/SqlInjectionAdvanced/quiz")
        self.client.get("WebGoat/JWT/secret/gettoken")

        # self.client.post("WebGoat/HttpBasics/attack1", {"person":"test"})
        # self.client.post("WebGoat/HttpBasics/attack2", {"answer":"POST", "magic_answer":"1", "magic_number":"1"})
        # self.client.post("WebGoat/SqlInjection/attack2", {"successMessage":"wrong"})
        # self.client.post("WebGoat/SqlInjection/attack2", {"query":"select * from employees where last_name='Franco';"})
        # self.client.post("WebGoat/SqlInjection/attack2", {"query":"select * from employees;"})
        # self.client.post("WebGoat/PasswordReset/SecurityQuestions", {"question":"In what city were you born?"})
        # self.client.post("WebGoat/InsecureLogin/task", {"usarname":"wrong", "password":"wrong"})
        # self.client.post("WebGoat/CrossSiteScripting/attack1", {"answer_xss_1":"Wd_qZOqb7SlDU4kuzbwqtUJm7dFuINr7vYa25PwQ"})
        # self.client.post("WebGoat/clientSideFiltering/getItForFree", {"checkoutCode":"abc"})
        # self.client.post("WebGoat/challenge/5", {"password_login":"pass", "remember":"on", "username_login":"larry"})

        # self.client.post("WebGoat/csrf/feedback/message")
        # self.client.post("WebGoat/auth-bypass/verify-account")
        # self.client.post("WebGoat/BypassRestrictions/FieldRestrictions")
        # self.client.post("WebGoat/BypassRestrictions/frontendValidation")
        # self.client.post("WebGoat/challenge/1")
        # self.client.post("WebGoat/challenge/5")
        # self.client.post("WebGoat/challenge/7")
        # self.client.post("WebGoat/ChromeDevTools/dummy")
        # self.client.post("WebGoat/ChromeDevTools/network")
        # self.client.post("WebGoat/ChromeDevTools/network")
        # self.client.post("WebGoat/cia/quiz")
        # self.client.post("WebGoat/clientSideFiltering/attack1")
        # self.client.post("WebGoat/clientSideFiltering/getItForFree")
        # self.client.post("WebGoat/CrossSiteScripting/attack1")
        # self.client.post("WebGoat/CrossSiteScripting/attack3")
        # self.client.post("WebGoat/CrossSiteScripting/attack4")
        # self.client.post("WebGoat/CrossSiteScripting/attack6a")
        # self.client.post("WebGoat/CrossSiteScripting/quiz")
        # self.client.post("WebGoat/CrossSiteScripting/phone-home-xss")
        # self.client.post("WebGoat/CrossSiteScripting/dom-follow-up")
        # self.client.post("WebGoat/CrossSiteScriptingStored/stored-xss-follow-up")
        # self.client.post("WebGoat/CrossSiteScriptingStored/stored-xss")
        # self.client.post("WebGoat/crypto/encoding/basic-auth")
        # self.client.post("WebGoat/crypto/hashing")
        # self.client.post("WebGoat/crypto/secure/defaults")
        # self.client.post("WebGoat/crypto/signing/verify")
        # self.client.post("WebGoat/crypto/encoding/xor")
        # self.client.post("WebGoat/csrf/confirm-flag-1")
        # self.client.post("WebGoat/csrf/feedback")
        # self.client.post("WebGoat/csrf/login")
        # self.client.post("WebGoat/csrf/review")
        # self.client.post("WebGoat/HtmlTampering/task")
        # self.client.post("WebGoat/HttpBasics/attack1")
        # self.client.post("WebGoat/HttpBasics/attack2")
        # self.client.post("WebGoatIDOR/diff-attributes")
        # self.client.post("WebGoat/IDOR/login")
        # self.client.post("WebGoatIDOR/profile/alt-path")
        # self.client.post("WebGoat/InsecureDeserialization/task")
        # self.client.post("WebGoat/InsecureLogin/task")
        # self.client.post("WebGoat/JWT/final/follow/admin")
        # self.client.post("WebGoat/JWT/final/delete")
        # self.client.post("WebGoat/JWT/refresh/login")
        # self.client.post("WebGoat/JWT/refresh/checkout")
        # self.client.post("WebGoat/JWT/refresh/newToken")
        # self.client.post("WebGoat/JWT/secret")
        # self.client.post("/JWT/votings/blue")
        # self.client.post("/JWT/votings")
        # self.client.post("/access-control/hidden-menu")
        
class WebsiteUser(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(0,5)