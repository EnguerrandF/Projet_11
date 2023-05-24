from locust import HttpUser, task 
import json


class PerfTest(HttpUser):
    def on_start(self):
        print("START")

    @task
    def perf_get_index(self):
        self.client.get("/")

    @task
    def perf_connexion_club(self):
        self.client.post("/showSummary",
                         {"email": "john@simplylift.com"})

    @task
    def perf_get_clubs(self):
        self.client.get("/clubs")

    @task
    def perf_get_book(self):
        self.client.get("/book/Spring Festival/Simply Lift")

    @task
    def perf_purchase_place(self):
        self.client.post("/purchasePlaces",
                         {"club": "Simply Lift",
                          "competition": "Spring Festival",
                          "places": 5})

    @task
    def perf_logout(self):
        self.client.get("/logout")

    def on_stop(self):
        print("END")
