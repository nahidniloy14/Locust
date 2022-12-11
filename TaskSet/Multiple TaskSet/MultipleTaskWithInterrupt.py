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
        self.interrupt(reschedule=False)  # It will have some breath time during execution


class ViewCart(SequentialTaskSet):
    @task
    def get_cart_items(self):
        print("Get all cart items")

    @task
    def search_cart_item(self):
        print("Searching item from cart")

    @task
    def exit_task_execution(self):
        self.interrupt(reschedule=False)#It will have some breath time during execution


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct, ViewCart]


#---Output----------------
# Searching men products
# Searching kids products
# Searching men products
# Searching kids products
# Get all cart items
# Searching item from cart

#Now it has reached to every task set
