# NOTE: Generated By HttpRunner v3.1.4
# FROM: gk_register.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseGkRegister(HttpRunner):

    config = (
        Config("测试用例：测试录入深圳地区-2021级-高起高职-小学教育专业成教嘉应学院学员业务流程")
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
            RunRequest("步骤一：使用测试账号登录测试>>>/loginByMobile.do")
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
            # .with_jmespath('hearder."Set-Cookie"',"Cookie_v")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
            .assert_equal("body.body", "SUCCESS")
        ),
        Step(
            RunRequest("步骤二：查询招生老师招生数据 >>>/recruit/findRecruitStudents.do")
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
            RunRequest("步骤三：打开录入学员信息页面 >>/recruit/toRecruitAdd.do")
            .get("/recruit/toRecruitAdd.do")
            .with_params(**{"recruitType": "2"})
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
            RunRequest("步骤四：查询手机号是否被注册 >>/recruit/getStudentInfoByMobile.do")
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
            RunRequest("步骤五：查询国开可报读城市信息 >>/baseinfo/getGkOpenEnrollCityInfo.do")
            .get("/baseinfo/getGkOpenEnrollCityInfo.do")
            .with_params(**{"page": "1", "rows": "7", "ext1": "5", "ext2": "202009"})
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
            RunRequest("步骤六：查询国开可报读院校信息 >>/baseinfo/sUnvs.do")
            .get("/baseinfo/sUnvs.do")
            .with_params(**{"page": "1", "rows": "7", "ext1": "2"})
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
            RunRequest("步骤七：查询国开可报读考区信息 >>/baseinfo/getOpenTestAreaByCity.do")
            .get("/baseinfo/getOpenTestAreaByCity.do")
            .with_params(
                **{
                    "page": "1",
                    "rows": "7",
                    "ext1": "440100",
                    "ext2": "5",
                    "ext3": "202009",
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
            RunRequest("步骤八：查询国开可报读专业信息 >>/baseinfo/getOpenPfsnByTaId.do")
            .get("/baseinfo/getOpenPfsnByTaId.do")
            .with_params(
                **{
                    "page": "1",
                    "rows": "7",
                    "ext1": "155184016465430588",
                    "ext2": "5",
                    "ext3": "202009",
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
            RunRequest("步骤九：获取国开优惠类型信息 >>/recruit/getScholarships.do")
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
            .with_data({"pfsnId": "158461564979445185", "taId": "155184016465430588"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
        Step(
            RunRequest("步骤十：获取国开学员报读专业收费标准信息 >>/recruit/showFeeList.do")
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
                    "pfsnId": "158461564979445185",
                    "taId": "155184016465430588",
                    "scholarship": "1",
                    "recruitType": "2",
                }
            )
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", "00")
        ),
        Step(
            RunRequest("步骤十一：招生老师录入国开学员信息 >>/recruit/recruitAdd.do")
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
            .upload(
            **{"stdId": "",
                "recruitType": "2",
                "nowProvinceName": "请选择",
                "nowCityName": "请选择",
                "nowDistrictName": "",
                "nowStreetName": "",
                "stdName": "自动化测试",
                "idType": "1",
                "idCard": "$new_id_card",
                "sex": "1",
                "birthday": "1992-10-07",
                "mobile": "$new_mobile",
                "nation": "",
                "politicalStatus": "",
                "rprType": "",
                "rprProvinceCode": "410000",
                "rprCityCode": "410100",
                "rprDistrictCode": "410102",
                "nowProvinceCode": "",
                "nowCityCode": "",
                "address": "",
                "jobStatus": "",
                "wpTime": "",
                "wpProvinceCode": "",
                "wpCityCode": "",
                "wpAddress": "",
                "wpTelephone": "",
                "zipCode": "450000",
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
                "grade": "202009",
                "city": "440100",
                "unvsId": "153959413805533477",
                "taId": "155184016465430588",
                "pfsnId": "158461564979445185",
                "secUnvsId": "",
                "scholarship": "1",
                "feeList": '[{"itemCode":"Y1","itemName":"代收第一年学费","amount":"1595.00","discount":"0.00","fdId":null,"odId":null,"payable":"1595.00","discountType":null,"orderNum":"2","itemYear":"1","itemType":"2","feeId":null,"itemSeq":null},{"itemCode":"S1","itemName":"代收第一年书费","amount":"250.00","discount":"0.00","fdId":null,"odId":null,"payable":"250.00","discountType":null,"orderNum":"3","itemYear":"1","itemType":"4","feeId":null,"itemSeq":null},{"itemCode":"W1","itemName":"代收第一年网络费","amount":"150.00","discount":"0.00","fdId":null,"odId":null,"payable":"150.00","discountType":null,"orderNum":"4","itemYear":"1","itemType":"5","feeId":null,"itemSeq":null},{"itemCode":"Y2","itemName":"代收第二年学费","amount":"1595.00","discount":"0.00","fdId":null,"odId":null,"payable":"1595.00","discountType":null,"orderNum":"5","itemYear":"2","itemType":"2","feeId":null,"itemSeq":null},{"itemCode":"S2","itemName":"代收第二年书费","amount":"250.00","discount":"0.00","fdId":null,"odId":null,"payable":"250.00","discountType":null,"orderNum":"6","itemYear":"2","itemType":"4","feeId":null,"itemSeq":null},{"itemCode":"W2","itemName":"代收第二年网络费","amount":"150.00","discount":"0.00","fdId":null,"odId":null,"payable":"150.00","discountType":null,"orderNum":"7","itemYear":"2","itemType":"5","feeId":null,"itemSeq":null},{"itemCode":"Y3","itemName":"代收第三年学费","amount":"1595.00","discount":"0.00","fdId":null,"odId":null,"payable":"1595.00","discountType":null,"orderNum":"8","itemYear":"3","itemType":"2","feeId":null,"itemSeq":null},{"itemCode":"S3","itemName":"代收第三年书费","amount":"250.00","discount":"0.00","fdId":null,"odId":null,"payable":"250.00","discountType":null,"orderNum":"9","itemYear":"3","itemType":"4","feeId":null,"itemSeq":null},{"itemCode":"W3","itemName":"代收第三年网络费","amount":"150.00","discount":"0.00","fdId":null,"odId":null,"payable":"150.00","discountType":null,"orderNum":"10","itemYear":"3","itemType":"5","feeId":null,"itemSeq":null},{"itemCode":"Y4","itemName":"代收第四年学费","amount":"1595.00","discount":"0.00","fdId":null,"odId":null,"payable":"1595.00","discountType":null,"orderNum":"11","itemYear":"4","itemType":"2","feeId":null,"itemSeq":null},{"itemCode":"S4","itemName":"代收第四年书费","amount":"250.00","discount":"0.00","fdId":null,"odId":null,"payable":"250.00","discountType":null,"orderNum":"12","itemYear":"4","itemType":"4","feeId":null,"itemSeq":null},{"itemCode":"W4","itemName":"代收第四年网络费","amount":"150.00","discount":"0.00","fdId":null,"odId":null,"payable":"150.00","discountType":null,"orderNum":"13","itemYear":"4","itemType":"5","feeId":null,"itemSeq":null},{"itemCode":"YS","itemName":"代收艺术加考费","amount":"0.00","discount":"0.00","fdId":null,"odId":null,"payable":"0.00","discountType":null,"orderNum":"100","itemYear":"","itemType":"3","feeId":null,"itemSeq":null}]',
                "feeId": "158513288558943818",
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
            RunRequest("步骤十二：查询录入的国开学员信息 >>/recruit/findRecruitStudents.do")
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
                    "year": "$new_mobile",
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
    TestCaseGkRegister().test_start()
