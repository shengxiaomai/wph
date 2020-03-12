from api.login import Login
import pytest

class TestLogin():
    def test_login(self):
        login=Login()
        token=login.login()
        print(token)
        assert token !=None