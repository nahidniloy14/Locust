from locust import User, between, task, TaskSet

class SearchProduct(TaskSet):
    @task
    def search_men_products(self):
        print("Searching men products")

    @task
    def search_kids_products(self):
        print("Searching kids products")

class MyUser(User):
    wait_time = between(1,2)
    tasks = [SearchProduct]
    #when task class is seperated from user class then we have to say the user class which tasks to execute
#Output:
# Searching kids products
# Searching men products
# Searching men products
# Searching kids products
# Searching men products
# Searching kids products
# Searching kids products
# Searching kids products
# Searching men products
# Searching men products
# Searching kids products
# Searching men products
# Searching men products
# Searching men products
# Searching men products
# Searching men products

#In this Case, There will be no such order of selection
