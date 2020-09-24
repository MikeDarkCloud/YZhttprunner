# NOTE: Generated By HttpRunner v3.1.4
# FROM: login.har
import pytest
from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase,Parameters


class TestCaseLogin(HttpRunner):
    # @pytest.mark.parametrize("param",Parameters({"mobile": [13560148201], "grade": ["2020"],"recruitType":[1]}),)
    # def test_start(self, param):
    #     super().test_start(param)


    def setup(self):
        print("开始")

    def teardown(self):
        print("结束")
    config = (Config("正向用例：测试我的学员页面搜索功能")
              .verify(False)
              .base_url("${ENV(BASE_URL)}")
              .variables(
                **{"mobile":"13560148201",
                   "grade":"2020",
                   "recruitType":"1",
                   }
    ))




    teststeps = [
        Step(
            RunRequest("步骤一：使用测试账号：${ENV(USERNAME)} 登录>>/loginByMobile.do")
                .post("/loginByMobile.do")
                .with_headers(
                **{
                    "Host": "pre-bms.yzwill.cn",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                }
            )
                .with_data(
                {
                    "isOpenImage": "",
                    "mobile": "${ENV(USERNAME)}",
                    "ImgValidCode": "",
                    "validCode": "${ENV(VCODE)}",
                }
            )
                # .extract()
                # .with_jmespath('hearder."Set-Cookie"', "var_Cookie")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal("body.code", "00")
                .assert_equal("body.body", "SUCCESS")
        ),
        Step(
            RunRequest("步骤二：进入助学管理-我的学员页面>>>/recruit/toStudentList.do")
                .get("/recruit/toStudentList.do")
                .with_headers(
                **{
                    "Host": "pre-bms.yzwill.cn",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                }
            )
                # .extract().with_regex()
                #.with_jmespath('"operatorId" value="(.*?)" />',"operatorId")
                # .with_jmespath('hearder."Set-Cookie"', "var_Cookie")
                .validate()
                .assert_equal("status_code", 200)
                .assert_equal('headers."Content-Type"', "text/html;charset=UTF-8")
        )
    ]


if __name__ == "__main__":
    TestCaseLogin().test_start()
