import pytest
# 前置后置 模块没生效(等同于class)   类等同于模块

class TestDemo05(object):

    def setup_class(self):
        print("执行所有方法之前先执行我一次：setup-class")

    def teardown_class(self):
        print('执行完所有方法之后执行我一次：teardwon-class')

    def setup_method(self):
        print("执行每个方法之前先执行我一次：setup-method")

    def teardown_method(self):
        print('执行每个方法之后执行我一次：teardwon-method')

    def setup(self):
        print("每个方法之前先执行我一次：setup-常规")

    def teardown(self):
        print('每个方法之后执行我一次：teardwon-常规')


    def test_one(self):
        print("第一个方法执行")
        str = 'huace'
        assert 'h' in str

    def test_two(self):
        print('第二个方法执行')
        x = 'xiao'
        assert 'x' in x









if __name__ == '__main__':
    pytest.main(['-vs'])