from locust import HttpLocust, TaskSet, task, between
import random, string
from random import choice, randint

class FullSet(TaskSet):

    @task
    def one_with_all(self):
        self.client.get("/owners/find")
        self.client.get("/owners/find?lastName=a")
        self.client.get("/owners/1")
        self.client.get("/owners/new")
        self.client.post("/owners/new", {"address":"addr", "city":"city", "firstName":"name", "lastName":''.join(random.choices(string.ascii_uppercase + string.digits, k=10)), "telephone":"555555"})
        self.client.get("/owners/7/edit")
        self.client.post("/owners/7/edit", data={"firstName": "John", "lastName": "Doe", "address": "Fake Street, 123", "city": "Springfield", "telephone": "ciccia"})
        self.client.get("/vets.html")
        self.client.get("/owners/3/pets/new")
        self.client.get("/owners/3/pets/1/edit")
        self.client.post("/owners/3/pets/new", data={"name": "pollo", "birthDate":"2019-10-27", "type": choice(["bird", "cat", "dog", "lizard", "snake", "hamster"])})
        self.client.get("/owners/7/pets/1/visits/new")
        self.client.get("/owners/7/pets/new")
        self.client.post("/owners/7/pets/10/visits/new", {"date":"2020-01-27","description":''.join(random.choices(string.ascii_uppercase + string.digits, k=10))})

class FullUser(HttpLocust):
    task_set = FullSet
    wait_time = between(0,5)
