# on_start>> called during when a user starts
# on_stop>> called during when a user stops
from locust import User, between, task


class MyUser(User):
    wait_time = between(1, 2)

    def on_start(self):
        print("MyUser : Hatching New User ..")

    @task
    def my_task1(self):
        print("task 1")

    def on_stop(self):
        print("MyUser : Deleting User ..")
