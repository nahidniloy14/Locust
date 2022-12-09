from locust import User, between, task, SequentialTaskSet


class SearchProduct(SequentialTaskSet):
    @task
    def search_men_products(self):
        print("Searching men products")

    @task
    def search_kids_products(self):
        print("Searching kids products")

    @task
    def exit_task_execution(self):
        self.interrupt()


class ViewCart(SequentialTaskSet):
    @task
    def get_cart_items(self):
        print("Get all cart items")

    @task
    def search_cart_item(self):
        print("Searching item from cart")

    @task
    def exit_task_execution(self):
        self.interrupt()


class MyUser(User):
    wait_time = between(1, 2)
    tasks = {
            SearchProduct: 4,
            ViewCart: 1
        }





