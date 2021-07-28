from locust import HttpLocust, TaskSet, task, between
import random, string


class UserBehaviour(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.client.verify = False
        self.start()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.stop()

    def start(self):
        self.client.get("")
        
    def stop(self):
        self.client.get("")

    @task
    def all_together(self):
        self.client.get("/cart")
        self.client.get("/account/password")
        self.client.get("/login")
        self.client.get("/login/forgotPassword")
        self.client.get("/login/resetPassword")
        self.client.get("/register")
        self.client.get("/account")
        self.client.get("/cart/mini")
        self.client.get("/cart/summary")
        self.client.get("/cart/add")
        self.client.get("/cart/empty")
        self.client.get("/product-quick-view")
        self.client.get("/search?q=t")
        self.client.get("/checkout")
        self.client.get("/checkout/login")
        self.client.get("/checkout/singleship")
        self.client.get("/checkout/multiship")
        self.client.get("/checkout/add-address")
        self.client.get("/contactus")
        self.client.get("/hot-sauces")
        self.client.get("/hot-sauces?mfg=Blair%27s")
        self.client.get("/search?q=hot")
        self.client.get("/search?q=sauce&sort=name%20asc")
        self.client.get("/search?q=red")
        self.client.get("/search?q=armageddon")
        self.client.get("/search?q=cold")
        self.client.get("/merchandise")
        self.client.get("/product-quick-view?id=100")
        self.client.get("/hot-sauces/day_of_the_dead_habanero_hot_sauce")
        self.client.get("/clearance")
        self.client.get("/clearance?sort=name%20asc")
        self.client.get("/clearance?sort=name%20desc")
        # FINO A QUI OK

class WebsiteUser(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(0, 5)