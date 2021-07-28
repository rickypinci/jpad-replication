from locust import HttpLocust, TaskSet, task, between
import random, string


class UserBehaviour(TaskSet):

    patient_uuid = "700578ae-0138-43c8-930a-ebd5b657e7fa"
    location_uuid = "aff27d58-a15c-49a6-9beb-d30dcfc0c66e"

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.start()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.stop()

    def start(self):
        #self.client.get("openmrs-standalone/ws/rest/v1/session")
        self.client.post("openmrs-standalone/login.htm", {"username": "admin", "password": "Admin123", "sessionLocation":"6"})

    def stop(self):
        self.client.get("openmrs-standalone/appui/header/logout.action?successUrl=openmrs-standalone")

    @task
    def get_session(self):
        self.client.get("openmrs-standalone/ws/rest/v1/session")
    
    @task
    def manage_person(self):
        person_uuid = "007037a0-0500-11e3-8ffd-0800200c9a66"
        self.client.get("openmrs-standalone/ws/rest/v1/person?q=john")
        self.client.get("openmrs-standalone/ws/rest/v1/person/"+ person_uuid)
        self.client.post("openmrs-standalone/ws/rest/v1/person/"+ person_uuid, json={"gender": "M","birthdate": "1997-01-13"})
        self.client.get("openmrs-standalone/ws/rest/v1/person/"+ person_uuid +"/attribute")
        self.client.get("openmrs-standalone/ws/rest/v1/person/"+ person_uuid +"/name")
        self.client.post("openmrs-standalone/ws/rest/v1/person" , json={
        
        "names": [
                    {
                    "givenName": "Mohit",
                    "familyName": "Kumar"
                    }
                ],
                "gender": "M",
                "birthdate": "1997-09-02",
                "addresses": [
                    {
                    "address1": "30, Vivekananda Layout, Munnekolal,Marathahalli",
                    "cityVillage": "Bengaluru",
                    "country": "India",
                    "postalCode": "560037"
                    }
                ]
        } )

    @task
    def manage_location(self):
        self.client.get("openmrs-standalone/ws/rest/v1/location?q=amani")
        resp = self.client.get("openmrs-standalone/ws/rest/v1/location/" + self.location_uuid)
        self.client.get("openmrs-standalone/ws/rest/v1/location/" + self.location_uuid + "/attribute")
        
        #create
        self.client.post("openmrs-standalone/ws/rest/v1/location" , json={
            "name": "Salzburg Hospital " + str(random.choices(string.ascii_uppercase + string.digits, k=10)),
            "description": "Salzburg hospital location",
            "address1": "Mullner House 48",
            "address2": "",
            "cityVillage": "salzburg",
            "stateProvince": "salzburg",
            "country": "Austria",
            "postalCode": "5020",
            "latitude": "",
            "longitude": "",
            "countyDistrict": "salzburg"
        }) 

        #update
        self.client.post("openmrs-standalone/ws/rest/v1/location/"+self.location_uuid, json=resp.json()) 
        
    @task
    def manage_patients(self):
        self.client.get("openmrs-standalone/ws/rest/v1/patient?q=UNKNOWN")
        self.client.get("openmrs-standalone/ws/rest/v1/patient/" + self.patient_uuid)


    @task
    def manage_visits(self):
        visit_uuid = "32516b63-9a12-4332-9dae-e581e7c30a28"
        req = self.client.get("openmrs-standalone/ws/rest/v1/visit/" + visit_uuid)
        self.client.get("openmrs-standalone/ws/rest/v1/visit/" + visit_uuid + "/attribute")
        self.client.get("openmrs-standalone/ws/rest/v1/visit?includeInactive=true")
        self.client.get("openmrs-standalone/ws/rest/v1/visit?includeInactive=false")
        self.client.post("openmrs-standalone/ws/rest/v1/visit", json={
            "patient": "700578ae-0138-43c8-930a-ebd5b657e7fa",
            "visitType": "7b0f5697-27e3-40c4-8bae-f4049abfb4ed",
            "startDatetime": "2016-10-08T04:09:25.000Z",
            "location": "aff27d58-a15c-49a6-9beb-d30dcfc0c66e",
            "indication": None
        })
        self.client.post("openmrs-standalone/ws/rest/v1/visit/"+visit_uuid, json=req.json())
        

    @task
    def manage_encounters(self):
        encounter_uuid = "d119fa65-415d-417e-8b25-28a592be0b97"
        self.client.get("openmrs-standalone/ws/rest/v1/encounter?q=john")
        resp = self.client.get("openmrs-standalone/ws/rest/v1/encounter/" + encounter_uuid)
        self.client.get("openmrs-standalone/ws/rest/v1/encounter/" + encounter_uuid + "/encounterprovider")
        self.client.post("openmrs-standalone/ws/rest/v1/encounter", json={
            "encounterDatetime": "2019-10-16 12:08:43",
            "patient": "700578ae-0138-43c8-930a-ebd5b657e7fa",
            "encounterType": "e22e39fd-7db2-45e7-80f1-60fa0d5a4378",
            "location": "aff27d58-a15c-49a6-9beb-d30dcfc0c66e",
            "encounterProviders": [{
                "provider": "b312bef3-f221-4189-ae4a-3bbc2e90a683",
                "encounterRole": "a0b03050-c99b-11e0-9572-0800200c9a66"
            }]
        })
        self.client.post("openmrs-standalone/ws/rest/v1/encounter/" + encounter_uuid, json=resp.json())



class WebsiteUser(HttpLocust):
    task_set = UserBehaviour
    wait_time = between(0, 5)