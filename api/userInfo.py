
import requests
from api import login
from api.BaseApi import BaseApi


class userInfo(BaseApi):
    URL="http://api.88ba.com"
    getCustomerDetailRoute = "/user/app/getCustomerDetail"
    getCustomerRoute="/user/app/getCustomerList"
    improveUserInfoRoute="/user/app/improveUserInfo"
    headers = {"authorization": login.Login.login(), "content - type": "application / json;charset = UTF - 8"}

    @classmethod
    def getCustomerList(self, pageSize,pageIndex):
        payload = {'pageSize':pageSize,"pageIndex":pageIndex}
        r = requests.get(self.URL + self.getCustomerRoute, params=payload, headers=self.headers, verify=False)
        self.json_data = r.json()
        self.verbose(self.json_data)
        return self.json_data

    @classmethod
    def getCustomerDetail(self,userId):
        payload = {'userId': userId}
        r=requests.get(self.URL + self.getCustomerDetailRoute, params=payload, headers=self.headers,verify=False)
        self.json_data = r.json()
        self.verbose(self.json_data)
        return self.json_data


    def improveUserInfo(self,params):
        r = requests.post(self.URL + self.improveUserInfoRoute, params=params, headers=self.headers, verify=False)
        self.json_data = r.json()
        self.verbose(self.json_data)
        return self.json_data