from locust import User, between, task, SequentialTaskSet


class SearchProduct(SequentialTaskSet):
    @task
    def search_men_products(self):
        print("Searching men products")

    @task
    def search_kids_products(self):
        print("Searching kids products")


class ViewCart(SequentialTaskSet):
    @task
    def get_cart_items(self):
        print("Get all cart items")

    @task
    def search_cart_item(self):
        print("Searching item from cart")


class MyUser(User):
    wait_time = between(1, 2)
    tasks =[SearchProduct,ViewCart]

#------Output-----------
# Get all cart items
# Searching item from cart
# Get all cart items
# Searching item from cart
# Get all cart items
# Searching item from cart
# Get all cart items
# Searching item from cart
# Get all cart items
# Searching item from cart


#It has selected only the items of view cart
#we have to find a way so that our program reaches to all the loops
#self.interrupt() with help us out
