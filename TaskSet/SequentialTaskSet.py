from locust import User, between, task, SequentialTaskSet


class SearchProduct(SequentialTaskSet):
    @task
    def search_men_products(self):
        print("Searching men products")

    @task
    def search_kids_products(self):
        print("Searching kids products")


class MyUser(User):
    # host if present
    wait_time = between(1, 2)
    tasks = [SearchProduct]

    # ----Output--------
# Searching kids products
# Searching men products
# Searching kids products
# Searching men products
# Searching kids products
# Searching men products
# Searching kids products
# Searching men products
# Searching kids products

# the output will maintain a sequence
