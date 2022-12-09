from locust import events
from AbstractClass import RegisteredUser
from AbstractClass import GuestUser

@events.test_start.add_listener
def on_test_start(**kwargs):
    print("......... Initiating Load Test ....... ON_TEST_START")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print("........ Load Test Completed ........ ON_TEST_END")


class UserGroupA(RegisteredUser):
    weight = 1
    RegisteredUser.tasks = []


class UserGroupB(GuestUser):
    weight = 4
    GuestUser.tasks = []






