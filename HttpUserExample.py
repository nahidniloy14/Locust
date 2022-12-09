from locust import between, task, SequentialTaskSet, HttpUser


class ViewCart(SequentialTaskSet):
    @task
    def get_all_cart_tem(self):
        with self.client.get("/index.php?controller=order", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Failed to get all cart items, StatusCode: " + str(response.status_code))
            else:
                if "Shopping-cart summary" in response.text:
                    response.success()
                else:
                    response.failure("Failed to get all cart items, Text: " + response.text)

    @task
    def exit_navigation(self):
        self.interrupt()


class MyUser(HttpUser):
    wait_time = between(1, 2)
    tasks = [ViewCart]




