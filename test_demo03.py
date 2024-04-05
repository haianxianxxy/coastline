# from test_pytest.test_demo02 import TestClass
import pytest


# def test_ss():
#     # 前置处理逻辑--webui测试
#     # 打开浏览器操作
#     test1 = TestClass()  # 实例化
#     test1.test_01()  # 登录
#     test1.test_02()  # 收藏
#     # 关闭浏览器

def test_one():
    print("第一个用例执行")
    st = 'huace'
    assert 'h' in st


def test_two():
    print('第二个用例执行')
    x = 'xiao'
    assert 'x' in x


if __name__ == '__main__':
    pytest.main(['-vs', '-k'])
