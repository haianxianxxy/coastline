import pytest
from selenium import webdriver
driver = webdriver.Chrome()
# 此处装饰的login函数 被fram_py/test_demo08里面的两个方法调用
@pytest.fixture()
def login():
    print("登录成功")   #前置

    yield                 #后置
    print('执行teardow')
    print('关闭浏览器')



@pytest.fixture(scope='session',autouse=True) #session 多个文件调用一次
def browser(request):
    global browser
    driver.path = r'D:\anzhuang\chromedriver_win32\chromedriver.exe'

