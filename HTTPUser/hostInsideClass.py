from locust import HttpUser, constant, task


class MyReqRes(HttpUser):
    #host = "https://regres.in"
    wait_time = constant(1)

    @task
    def get_users(self):
        response=self.client.get("/api/users?page=2")
        print(response.text)
        print(response.status_code)
        print(response.headers)



    @task
    def create_user(self):
        self.client.post("/api/users", data=
        {"name": "morpheus", "job": "leader"}
                         )
