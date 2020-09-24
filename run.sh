#!/bin/bash

path="/home/www/webapp/AutoTest/testcases"

rm -rf /home/www/webapp/AutoTest/testcases/allure-results

cd $path && pytest --alluredir allure-results

echo "接口测试已经完成，正在生成报告......"
