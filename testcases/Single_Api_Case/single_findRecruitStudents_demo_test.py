# NOTE: Generated By HttpRunner v3.1.4
# FROM: login.har
import pytest
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase,Parameters


class TestCaseLogin(HttpRunner):
    # @pytest.mark.parametrize("param",Parameters({"mobile": [13560148201], "grade": ["2020"],"recruitType":[1]}),)
    # def test_start(self, param):
    #     super().test_start(param)
    config = (Config("正向用例：测试我的学员页面搜索功能")
              .verify(False)
              .base_url("${ENV(BASE_URL)}")
              .variables(
                **{"mobile":"13560148201",
                   "grade":"2020",
                   "recruitType":"1",
                   "headers":"${get_headers()}",
                   }
    ))
    teststeps = [
        Step(
            RunRequest("步骤一：使用测试账号：${ENV(USERNAME)} 登录>>/loginByMobile.do")
                .post("/loginByMobile.do")
                .with_headers()
                .with_data(
                {
                    "isOpenImage": "",
                    "mobile": "${ENV(USERNAME)}",
                    "ImgValidCode": "",
                    "validCode": "${ENV(VCODE)}",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", "00")
                .assert_equal("body.body", "SUCCESS")
        ),
        Step(
            RunRequest("步骤二：打开我的学员页面默认搜索学员数据>>>/recruit/findRecruitStudents.do")
                .post("/recruit/findRecruitStudents.do")
                .with_headers()
                .with_data(
                {
                    "start": "0",
                    "length": "10",
                    "loginName": "蓝明勇",
                    "operatorId": "153942325141232743",
                    "stdName": "",
                    "idCard": "",
                    "mobile": "$mobile",
                    "year": "",
                    "grade": "2020",
                    "unvsId": "",
                    "pfsnLevel": "",
                    "isDataCompleted": "",
                    "stdStage": "",
                    "recruitType": "1",
                    "sg": "",
                    "scholarship": "",
                    "inclusionStatus": "",
                    "taName": "",
                    "recruitName": "蓝明勇",
                    "recruitStatus": "",
                    "assignFlag": "",
                    "stdType": "",
                    "remark": "",
                    "ifBind": "",
                    "yearArrears": "",
                    "empId": "",
                    "myAnnexStatus": "",
                    "isPay": "",
                    "gkEntranceTest": "",
                    "isReturnSchool": "",
                }
            )
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", "00")
        )
    ]


if __name__ == "__main__":
    TestCaseLogin().test_start()