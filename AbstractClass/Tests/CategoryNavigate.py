from locust import task, SequentialTaskSet



class CategoryNavigate(SequentialTaskSet):
    @task
    def navigate_to_women_category(self):
        print("Navigating to woman catagory")
    @task
    def navigate_to_dresses_category(self):
        print("Navigating to dresses catagory")
    @task
    def navigate_to_shirt_category(self):
        print("Navigating to shirt catagory")
    @task
    def exit_task_execution(self):
        self.interrupt()
