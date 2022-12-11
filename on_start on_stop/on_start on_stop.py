from locust import User, between, task, SequentialTaskSet, events

# execute exactly once before and after suit
@events.test_start.add_listener
def on_test_start(**kwargs):
    print("......... Initiating Load Test ....... ON_TEST_START")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print("........ Load Test Completed ........ ON_TEST_END")

# execute for each user locast hatch

class SearchProduct(SequentialTaskSet):

    def on_start(self):
        print("SearchProduct : Tasks execution started ..")

    def on_stop(self):
        print("SearchProduct : Tasks execution completed ..")

    @task
    def search_men_products(self):
        print("Searching men products")

    @task
    def search_kids_products(self):
        print("Searching kids products")

    @task
    def exit_task_execution(self):
        self.interrupt()

#execute for each taskset execution
class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct]

    def on_start(self):
        print("MyUser : Hatching New User ..")

    def on_stop(self):
        print("MyUser : Deleting User ..")



# ......... Initiating Load Test .......

# [2022-12-09 09:00:26,925] NahidNiloy14/INFO/locust.runners: Ramping to 1 users at a rate of 1.00 per second
# [2022-12-09 09:00:26,932] NahidNiloy14/INFO/locust.runners: All users spawned: {"MyUser": 1} (1 total users)
# MyUser : Hatching New User ..
# SearchProduct : Tasks execution started ..
# Searching men products
# Searching kids products
# SearchProduct : Tasks execution completed ..
# SearchProduct : Tasks execution started ..
# Searching men products
# Searching kids products
# SearchProduct : Tasks execution completed ..
# SearchProduct : Tasks execution started ..
# Searching men products
# Searching kids products
# SearchProduct : Tasks execution completed ..
# SearchProduct : Tasks execution started ..
# Searching men products
# Searching kids products
# SearchProduct : Tasks execution completed ..
# SearchProduct : Tasks execution started ..
# MyUser : Hatching Deleting User ..

# ........ Load Test Completed ........ ON_TEST_END