from locust import User, between, task, TaskSet, constant


class SearchProduct(TaskSet):
    # weight=2
    # wait_time=constant(2)
    @task(4)
    def search_men_products(self):
        print("Searching men products")

    @task(1)
    def search_kids_products(self):
        print("Searching kids products")


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct]

# Searching men products
# Searching men products
# Searching men products
# Searching kids products
# Searching men products
# Searching men products
# Searching men products

# giving more weight to the task indicates that there are more chances to be picked up
# in this case Searching men products is an example
