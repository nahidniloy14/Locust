import csv
import os


class UserInfo:
    user_list = []
    csv_file_path = os.getcwd() + "CSV/user.csv"

    @staticmethod
    def load_users():
        reader = csv.DictReader(open(UserInfo.csv_file_path))
        for line_elem in reader:
            UserInfo.user_list.append(line_elem)

    @staticmethod
    def get_user():
        if len(UserInfo.user_list) < 1:
            UserInfo.load_users()
        user_obj = UserInfo.user_list.pop()
        return user_obj

class Cookies:
    @staticmethod
    def get_base_header():
        base_header = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive'
        }
        return base_header

    @staticmethod
    def get_base_header_with_cookie(cookie):
        cookie_header = cookie.get_base_header()
        cookie_str = ""
        for item in cookie.iteritems():
            cookie_str += item[0] + "=" + item[1]
        cookie_header['Cookie'] = cookie_str
        return cookie_header




