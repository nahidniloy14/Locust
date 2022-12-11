from locust import between

from Abstract.Users import AbstractUser


class GuestHttpUser(AbstractUser):
    wait_time = between(1, 2)
    abstract = True

    def on_start(self):
        pass

    def on_stop(self):
        pass

