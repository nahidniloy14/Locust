from locust import User, between, task, SequentialTaskSet, events


@events.test_start.add_listener
def on_test_start(**kwargs):
    print("......... Initiating Load Test ....... ON_TEST_START")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print("........ Load Test Completed ........ ON_TEST_END")


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


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct]

    def on_start(self):
        print("MyUser : Hatching New User ..")

    def on_stop(self):
        print("MyUser : Deleting User ..")



