# NOTE: Generated By HttpRunner v3.1.4
# FROM: har\zk_student_register.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseZkStudentRegister(HttpRunner):

    config = (
        Config("测试用例：测试录入广州地区-2021级-专升本-汉语言文学专业暨南大学（自考）学员业务流程")
        .verify(False)
        .base_url("${ENV(BASE_URL)}")
        .variables(
            **{
                "new_mobile":"${get_mobile()}",
                "new_id_card":"${create_identity()}"
            }
        )
        )

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
            .extract()
            .with_jmespath('hearder."Set-Cookie"', "var_Cookie")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
            .assert_equal("body.body", "SUCCESS")
        ),
        Step(
            RunRequest("步骤二：登录获取优惠类型>>>>/baseinfo/scholarship.do")
            .post("/baseinfo/scholarship.do")
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
            .with_data("")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
        Step(
            RunRequest("步骤四：进入助学管理-我的学员页面>>>>/recruit/toStudentList.do")
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
            .validate()
            .assert_equal("status_code", 200)
        ),
        Step(
            RunRequest("步骤五：打开我的学员页面默认搜索学员数据>>>/recruit/findRecruitStudents.do")
            .post("/recruit/findRecruitStudents.do")
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
                    "start": "0",
                    "length": "10",
                    "loginName": "蓝明勇",
                    "operatorId": "153942325141232743",
                    "stdName": "",
                    "idCard": "",
                    "mobile": "",
                    "year": "2021",
                    "grade": "",
                    "unvsId": "",
                    "pfsnLevel": "",
                    "isDataCompleted": "",
                    "stdStage": "",
                    "recruitType": "",
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
        ),
        Step(
            RunRequest("步骤六：获取所有院系数据>>>/bdUniversity/findAllKeyValue.do")
            .get("/bdUniversity/findAllKeyValue.do")
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
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
        Step(
            RunRequest("步骤八：获取自考考区>>>/recruit/getZkFormalApplyArea.do")
            .post("/recruit/getZkFormalApplyArea.do")
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
            .with_data({"rows": "200", "page": "1"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
        Step(
            RunRequest("步骤九：根据学员手机号获取学员信息>>>/recruit/getStudentInfoByMobile.do")
            .post("/recruit/getStudentInfoByMobile.do")
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
            .with_data({"mobile": "$new_mobile"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
        Step(
            RunRequest("步骤十：自考获取可报读院校信息>>>/baseinfo/sUnvs.do")
            .get("/baseinfo/sUnvs.do")
            .with_params(
                **{"page": "1", "rows": "10", "sName": "", "ext1": "4", "ext2": "1"}
            )
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
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
        Step(
            RunRequest("步骤十：自考根据专业获取优惠类型>>>/baseinfo/sPfsnByOnScholarship.do")
            .get("/baseinfo/sPfsnByOnScholarship.do")
            .with_params(
                **{
                    "sId": "158562385344880832",
                    "ext1": "1",
                    "ext2": "2021",
                    "page": "1",
                    "rows": "10",
                    "sName": "",
                }
            )
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
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
        Step(
            RunRequest("步骤十一：自考获取可报读考试城市信息>>>/activityUnvsInfo/getZkCity.do")
            .post("/activityUnvsInfo/getZkCity.do")
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
            .with_data({"pfsnId": "158562577073954021"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
        Step(
            RunRequest("步骤十二：自考获取可报读考试城市编码信息>>>/baseinfo/getTaByCityCode.do")
            .post("/baseinfo/getTaByCityCode.do")
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
                    "rows": "10",
                    "page": "3",
                    "cityId": "440100",
                    "pfsnId": "158562577073954021",
                    "sName": "",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
        Step(
            RunRequest("步骤十三：自考获取可报读优惠类型信息>>>/recruit/getScholarships.do")
            .post("/recruit/getScholarships.do")
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
            .with_data({"pfsnId": "158562577073954021", "taId": "164"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
        Step(
            RunRequest("步骤十四：自考获取报读收费标准信息>>>/recruit/showFeeList.do")
            .post("/recruit/showFeeList.do")
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
                    "recruitType": "4",
                    "taId": "164",
                    "pfsnId": "158562577073954021",
                    "scholarship": "77",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
        Step(
            RunRequest("步骤十五：自考报读获得招生老师信息>>>/recruit/getRecruitInfo.do")
            .post("/recruit/getRecruitInfo.do")
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
            .with_data({"pfsnId": "158562577073954021", "scholarship": "77"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
        Step(
            RunRequest("步骤十六：自考学员信息后台录入手机号>>>/recruit/recruitAdd.do")
            .post("/recruit/recruitAdd.do")
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
                    "recruitType": "4",
                    "stdName": "自考自动化测试",
                    "idType": "1",
                    "idCard": "$new_id_card",
                    "sex": "1",
                    "birthday": "1990-03-07",
                    "mobile": "$new_mobile",
                    "health": "0",
                    "maritalStatus": "1",
                    "nation": "01",
                    "politicalStatus": "13",
                    "rprType": "1",
                    "address": "猎德冼村1号",
                    "jobType": "11",
                    "wpTime": "",
                    "cadrePosition": "5",
                    "technicalPosition": "4",
                    "companyType": "3",
                    "wpAddress": "",
                    "wpTelephone": "",
                    "zipCode": "574100",
                    "telephone": "",
                    "email": "",
                    "qq": "",
                    "wechat": "",
                    "jobTitle": "",
                    "workPlace": "",
                    "remark": "",
                    "edcsType": "1",
                    "unvsName": "",
                    "adminssionTime": "",
                    "graduateTime": "",
                    "profession": "",
                    "diploma": "",
                    "edcsSystem": "",
                    "examineRegister": "",
                    "pfsnLevel": "1",
                    "unvsId": "158562385344880832",
                    "pfsnId": "158562577073954021",
                    "cityId": "440100",
                    "taId": "164",
                    "formalTaId": "0106",
                    "scholarship": "77",
                    "feeExplain": "",
                    "pfsnName": "汉语言文学",
                    "pfsnCode": "JN202102HYYW(ZK)",
                    "feeId": "158562541195142423",
                    "feeName": "暨南大学（自）(10559)-2021级-保障本科11980",
                    "offerId": "",
                    "offerName": "",
                    "offerRemark": "",
                    "feeTotal": "11980.00",
                    "feeList": '[{"itemCode":"P0","itemName":"培训费","amount":"11980.00","discount":"0.00","fdId":null,"odId":null,"payable":"11980.00","discountType":null,"orderNum":"101","itemYear":"0","itemType":"1","feeId":null,"itemSeq":null}]',
                    "givePfsnLevel": "1",
                    "giveActId": "68",
                    "giveUnvsName": "嘉应学院",
                    "giveUnvsCode": "10582",
                    "givePfsnName": "汉语言文学",
                    "grade": "2021",
                    "givePfsnId": "156879308510845271",
                    "giveUnvsId": "1",
                    "giveGrade": "2021",
                    "gradeYear": "2021",
                    "nowProvinceCode": "19",
                    "nowCityCode": "1601",
                    "nowDistrictCode": "3633",
                    "nowProvinceName": "广东省",
                    "nowCityName": "广州市",
                    "nowDistrictName": "天河区",
                    "rprProvinceCode": "440000",
                    "rprCityCode": "440100",
                    "rprDistrictCode": "440101",
                    "rprProvinceName": "广东省",
                    "rprCityName": "广州市",
                    "rprDistrictName": "市辖区",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
    ]


if __name__ == "__main__":
    TestCaseZkStudentRegister().test_start()
