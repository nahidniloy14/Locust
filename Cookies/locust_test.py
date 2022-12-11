from locust import events

from Abstract.Tests.CategoryNavigate import CategoryNavigate
from Abstract.Users import GuestUser, RegisteredUser


@events.test_start.add_listener
def on_test_start(**kwargs):
    print("......... Initiating Load Test ....... ON_TEST_START")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print("........ Load Test Completed ........ ON_TEST_END")


class UserGroupA(RegisteredUser):
    weight = 1
    RegisteredUser.tasks = [CategoryNavigate]







