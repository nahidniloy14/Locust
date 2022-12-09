from locust import between, clients
from AbstractClass import AbstractUser


class RegisteredHttpUser(AbstractUser):
    wait_time = between(1, 2)
    abstract = True  #its coming from Abstract User

    def __init__(self, parent):#constructor
        super(AbstractUser, self).__init__(parent)
        self.user_attr = None #will store the login infos later

    def on_start(self):
        # TODO: Fetch one user from user list and login, store cookie and user info
        pass

    def on_stop(self):
        # TODO: Logout user from server when load test ends
        pass








