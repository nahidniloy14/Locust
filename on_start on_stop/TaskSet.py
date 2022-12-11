from locust import SequentialTaskSet, task


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
