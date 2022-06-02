import requests


class ClassForTest:
    def send_request(self):
        response = requests.get("https://test.com")
        return response