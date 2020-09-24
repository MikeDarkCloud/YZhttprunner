# NOTE: Generated By HttpRunner v3.1.4
# FROM: har\cj_student_register.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseCjStudentRegister(HttpRunner):

    config = (
        Config("测试用例：测试招生录入成教学员业务流程")
        .verify(False)
        .base_url("${ENV(BASE_URL)}")
        .variables(
            **{
                "new_mobile":"${get_mobile()}",
                "new_id_card": "${create_identity()}"
            }
        )
              )

    teststeps = [
        Step(
            RunRequest("步骤一：使用测试账号：'${ENV(USERNAME)}'登录>>/loginByMobile.do")
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
            # .with_jmespath('hearder."Set-Cookie"',"var_Cookie")
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
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal('headers."Content-Type"', "text/html;charset=UTF-8")
        ),
        Step(
            RunRequest("步骤三：进入助学管理-添加学员>>>/recruit/toRecruitAdd.do")
            .get("/recruit/toRecruitAdd.do")
            .with_params(**{"recruitType": "1"})
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
            RunRequest("步骤四：根据手机号获取学员信息>>>/recruit/getStudentInfoByMobile.do")
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
            RunRequest("步骤五：获取可报读院校信息>>>/baseinfo/sUnvs.do")
            .get("/baseinfo/sUnvs.do")
            .with_params(**{"page": "1", "rows": "7", "ext1": "1"})
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
            RunRequest("步骤六：根据优惠类型获取可报读专业信息>>>/baseinfo/sPfsnByOnScholarship.do")
            .get("/baseinfo/sPfsnByOnScholarship.do")
            .with_params(
                **{"page": "1", "rows": "7", "sId": "1", "ext1": "5", "ext2": "2021"}
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
            RunRequest("步骤七：获取可报读考区信息>>>/baseinfo/sTaNotStop.do")
            .get("/baseinfo/sTaNotStop.do")
            .with_params(**{"page": "1", "rows": "7", "sId": "156879274020353161"})
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
            RunRequest("步骤八：获取优惠类型信息>>>/recruit/getScholarships.do")
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
            .with_data({"pfsnId": "156879274020353161", "taId": "153680559369877483"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
        Step(
            RunRequest("步骤九：获取收费标准信息>>>/recruit/showFeeList.do")
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
                    "pfsnId": "156879274020353161",
                    "taId": "153680559369877483",
                    "scholarship": "71",
                    "recruitType": "1",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
        Step(
            RunRequest("步骤十：成教学员信息录入，学员手机号：$var_mobile >>>/recruit/recruitAdd.do")
            .post("/recruit/recruitAdd.do")
            .with_headers(
                **{
                    "Host": "pre-bms.yzwill.cn",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                    "Connection": "keep-alive",
                }
            )
            .upload(**{
                    "stdId": "",
                    "recruitType": "1",
                    "nowProvinceName": "广东省",
                    "nowCityName": "广州市",
                    "nowDistrictName": "天河区",
                    "nowStreetName": "",
                    "stdName": "自动化测试",
                    "idType": "1",
                    "idCard": "$new_mobile",
                    "sex": "1",
                    "birthday": "1990-03-07",
                    "mobile": "$new_id_card",
                    "nation": "01",
                    "politicalStatus": "13",
                    "rprType": "1",
                    "rprAddressCode": "440101",
                    "nowProvinceCode": "19",
                    "nowCityCode": "1601",
                    "nowDistrictCode": "3633",
                    "address": "西乡街道草围二路20号新宜家超市",
                    "jobType": "11",
                    "wpTime": "",
                    "wpProvinceCode": "",
                    "wpCityCode": "",
                    "wpAddress": "",
                    "wpTelephone": "",
                    "zipCode": "100000",
                    "emergencyContact": "",
                    "headPic": "",
                    "headPortrait": "",
                    "isPhotoChange": "",
                    "telephone": "",
                    "email": "",
                    "qq": "",
                    "wechat": "",
                    "jobTitle": "",
                    "workPlace": "",
                    "maritalStatus": "",
                    "remark": "",
                    "edcsType": "",
                    "unvsName": "",
                    "oldProvinceCode": "",
                    "oldCityCode": "",
                    "adminssionTime": "",
                    "graduateTime": "",
                    "profession": "",
                    "diploma": "",
                    "edcsSystem": "",
                    "oldEducationName": "",
                    "oldEducationNum": "",
                    "materialCode": "",
                    "pfsnLevel": "5",
                    "enrollType": "1",
                    "grade": "2021",
                    "unvsId": "1",
                    "pfsnId": "156879274020353161",
                    "taId": "153680559369877483",
                    "secUnvsId": "",
                    "bpType": "3",
                    "points": "20",
                    "scholarship": "71",
                    "feeList": '[{"itemCode":"Y0","itemName":"考前辅导费","amount":"299.00","discount":"0.00","fdId":null,"odId":null,"payable":"299.00","discountType":null,"orderNum":"1","itemYear":"0","itemType":"1","feeId":null,"itemSeq":null},{"itemCode":"Y1","itemName":"代收第一年学费","amount":"2300.00","discount":"0.00","fdId":null,"odId":null,"payable":"2300.00","discountType":null,"orderNum":"2","itemYear":"1","itemType":"2","feeId":null,"itemSeq":null},{"itemCode":"S1","itemName":"代收第一年书费","amount":"400.00","discount":"0.00","fdId":null,"odId":null,"payable":"400.00","discountType":null,"orderNum":"3","itemYear":"1","itemType":"4","feeId":null,"itemSeq":null},{"itemCode":"Y2","itemName":"代收第二年学费","amount":"2300.00","discount":"0.00","fdId":null,"odId":null,"payable":"2300.00","discountType":null,"orderNum":"5","itemYear":"2","itemType":"2","feeId":null,"itemSeq":null},{"itemCode":"S2","itemName":"代收第二年书费","amount":"400.00","discount":"0.00","fdId":null,"odId":null,"payable":"400.00","discountType":null,"orderNum":"6","itemYear":"2","itemType":"4","feeId":null,"itemSeq":null},{"itemCode":"Y3","itemName":"代收第三年学费","amount":"1150.00","discount":"0.00","fdId":null,"odId":null,"payable":"1150.00","discountType":null,"orderNum":"8","itemYear":"3","itemType":"2","feeId":null,"itemSeq":null},{"itemCode":"S3","itemName":"代收第三年书费","amount":"200.00","discount":"0.00","fdId":null,"odId":null,"payable":"200.00","discountType":null,"orderNum":"9","itemYear":"3","itemType":"4","feeId":null,"itemSeq":null},{"itemCode":"YS","itemName":"代收艺术加考费","amount":"0.00","discount":"0.00","fdId":null,"odId":null,"payable":"0.00","discountType":null,"orderNum":"100","itemYear":"","itemType":"3","feeId":null,"itemSeq":null}]',
                    "feeId": "156888459970824434",
                    "offerId": "",
                    "enrollUnvsName": "",
                    "pfsnName": "",
                    "pfsnCode": "",
                    "taName": "",
                })
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")

        ),
        Step(
            RunRequest("步骤十一：查询助学老师学员信息 >>>/recruit/findRecruitStudents.do")
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
    ]


if __name__ == "__main__":
    TestCaseCjStudentRegister().test_start()
