from locust import events

from AbstractClass.Tests.CategoryNavigate import CategoryNavigate
from AbstractClass.Users import GuestUser, RegisteredUser


@events.test_start.add_listener
def on_test_start(**kwargs):
    print("......... Initiating Load Test ....... ON_TEST_START")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print("........ Load Test Completed ........ ON_TEST_END")


class UserGroupA(RegisteredUser):
    weight = 1
    RegisteredUser.tasks = [CategoryNavigate]







