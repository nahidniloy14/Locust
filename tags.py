
from locust import HttpUser, task, constant, SequentialTaskSet, tag


class MyScript(SequentialTaskSet):

    @task
    @tag('xml','get')
    def get_xml(self):
        result = self.client.get("/xml", name="XML")
        print(result)

    @task
    @tag('get','json')
    def get_json(self):
        expected_response = "Wake up to WonderWidgets!"
        with self.client.get("/json", catch_response=True, name="JSON") as response:
            result = True if expected_response in response.text else False  # Pythonic if else statement
            print(self.get_json.__name__, result)  # Prints True if the response contains expected_response
            response.success()  # Marking this as success
            # response.failure()  # Marking this as failure

class MyLoadTest(HttpUser):
    host="https://httbin.org"
    wait_time = constant(1)
    tasks = [MyScript]

    #--------------Run tags----------------------------
    # locust -f main.py -u 1 -r 1 -t=10s --headless --tags get
    # locust -f main.py -u 1 -r 1 -t=10s --headless --exclude-tags get