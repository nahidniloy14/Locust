#on_start>> when the taskset starts executing
#on_stop>> when the taskset stops executing

from locust import SequentialTaskSet, task, User, between


class SearchProduct(SequentialTaskSet):

    def on_start(self):
        print("SearchProduct : Tasks execution started ..")

    @task
    def search_men_products(self):
        print("Searching men products")

    @task
    def search_kids_products(self):
        print("Searching kids products")

    @task
    def exit_task_execution(self):
        self.interrupt()

    def on_stop(self):
        print("SearchProduct : Tasks execution completed ..")

class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct]

# SearchProduct : Tasks execution started
# Searching men products
# Searching kids products
# SearchProduct : Tasks execution completed
# SearchProduct : Tasks execution started
# Searching men products
# Searching kids products
# SearchProduct : Tasks execution completed
# SearchProduct : Tasks execution started
# Searching men products
# Searching kids products
# SearchProduct : Tasks execution completed
