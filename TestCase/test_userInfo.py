
from api import userInfo
import pytest
import allure
import logging

class TestUserInfo:

    @allure.story("APP用户相关资料模块 查询客户列表")
    @pytest.mark.parametrize("pageSize,pageIndex",[(10,1)])
    def test_getCustomerList(self,pageSize,pageIndex):
        logging.info("调用接口获取json_data")
        json_data = userInfo.userInfo.getCustomerList(pageSize,pageIndex)
        if ("status" in json_data):
            assert json_data["status"] < 2000
        else:
            assert json_data["totalCount"] >= 0
            return json_data["customerDataList"][0]["userID"]

    @allure.story("APP用户相关资料模块 查询客户详情")
    @pytest.mark.parametrize("userId", [266836055947215278])
    def test_getCustomerDetail(self,userId):
        json_data=userInfo.userInfo.getCustomerDetail(userId)
        if("status" in json_data):
            assert json_data["status"] < 2000
        else:
            assert json_data["userId"] ==  266836055947215278

    @allure.story("APP用户相关资料模块 查询客户详情")
    @pytest.mark.parametrize("params", [{ "avatar": "test.jpg", "city": "r城市", "cityId": "1", "name": "test",
                                          "province": "广西", "provinceId": "1", "roleType": "1",
                                          "sex": 1,"userId": "string"}])
    def test_improveUserInfo(self, params):
        json_data = userInfo.userInfo.improveUserInfo(params)
        if ("status" in json_data):
            assert json_data["status"] < 2000
        else:
            assert json_data["totalCount"] >= 0
