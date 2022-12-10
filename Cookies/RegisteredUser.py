from locust import between
from AbstractClass.Users import AbstractUser
from Cookies import DataLoad
from Cookies import *

class RegisteredHttpUser(AbstractUser):
    wait_time = between(1, 2)
    abstract = True  #its coming from Abstract User

    def __init__(self, parent):#constructor
        super(AbstractUser, self).__init__(parent)
        self.user_attr = None #will store the login infos later

    def on_start(self):
        user_obj = DataLoad.UserInfo.get_user()
        form_data = {'email': user_obj['username'], 'passwd': user_obj['password'],
                     'back': 'my-account', 'SubmitLogin': ''}

        with self.client.post("/index.php?controller=authentication", form_data, headers=DataLoad.Cookies.get_base_header(),
                              catch_response=True) as response:
            if self.verify_login_success(response, user_obj['username']):
                super().set_email(user_obj['username'])
                super().set_cookie(response.cookies)
                print(DataLoad.Cookies.get_base_header_with_cookie(response.cookies))

        pass

    def on_stop(self):
        # TODO: Logout user from server when load test ends
        pass








