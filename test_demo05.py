import pytest


# 前置后置 类


class TestDemo05(object):

    def setup_class(self):
        print("执行所有方法之前先执行我一次：setup")

    def teardown_class(self):
        print("执行完所有方法之后执行我一次：teardwon")

    def test_one(self):
        print("第一个方法执行")
        st = 'huace'
        assert 'h' in st

    def test_two(self):
        print("第二个方法执行")
        x = "xiao"
        assert "x" in x



if __name__ == '__main__':
    pytest.main(['-vs'])
