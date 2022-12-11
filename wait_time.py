import time

from locust import User, task, between, constant, constant_pacing


class task1(User):
    wait_time = constant(1)
    @task
    def my_task1(self):
        print("This will inject 1 sec delay")


class task2(User):
    wait_time = between(1,2) #time between two execution
    @task
    def my_task2(self):
        print("This will inject minimum 2 sec delay and maximum 5 sec delay")


class task3(User):
    wait_time = constant_pacing(5) #time between two execution
    @task
    def my_task3(self):
        time.sleep(3)
        print("This will ignore time.sleep() and inject 5 sec delay")


class task4(User):
    @task
    def my_task4(self):
        time.sleep(3)
        print("This will inject 3 sec delay")

