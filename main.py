from locust import User, task, between

class Myuser(User):
    wait_time = between(1,2) #time between two execution

    @task
    def my_task1(self):
        print("task 1")

    @task
    def my_task2(self):
        print("task 2")

