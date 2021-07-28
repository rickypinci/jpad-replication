import time
from locust import HttpUser, task, between

AUTH = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmZHNlX21pY3Jvc2VydmljZSIsInJvbGVzIjpbIlJPTEVfVVNFUiJdLCJpZCI6IjRkMmE0NmM3LTcxY2ItNGNmMS1iNWJiLWI2ODQwNmQ5ZGE2ZiIsImlhdCI6MTYyNjM1Njc0OSwiZXhwIjoxNjI2MzYwMzQ5fQ.KSV0KRAuJOioX40s6yq6a6CfPxhAk8VjrEifFQThO_U"

class QuickstartUser(HttpUser):
	wait_time = between(1, 3)

#	def on_start(self):
#		self.client.post("api/v1/users/login", json={"password":"111111", "username":"fdse_microservice", "verificationCode":""})
	
	@task
	def bookTrain(self):
		self.client.get("index.html")
		self.client.post("api/v1/travelservice/trips/left", json={"departureTime":"2021-07-08", "endPlace":"Su Zhou", "startingPlace":"Shang Hai"})
		self.client.get("client_ticket_book.html?tripId=D1345&from=Shang Hai&to=Su Zhou&seatType=2&seat_price=50.0&date=2021-07-08")
		self.client.post("api/v1/preserveservice/preserve", json={"accountId":"4d2a46c7-71cb-4cf1-b5bb-b68406d9da6f","contactsId":"8e72fc88-beff-4a70-bcb3-4fbf38168e5c","tripId":"D1345","seatType":"2","date":"2021-07-08","from":"Shang Hai","to":"Su Zhou","assurance":"0","foodType":2,"stationName":"suzhou","storeName":"Roman Holiday","foodName":"Spicy hot noodles","foodPrice":5}, headers={"Authorization":AUTH})
