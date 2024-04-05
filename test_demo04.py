import pytest
# 前置后置 函数   函数不在类中


def setup_function():
    print("执行每个函数之前先执行我一次：setup")


def teardown_function():
    print('执行每个函数之后执行我一次 teardwon')


def test_one():                 # 执行这个函数前先执行setup  之后再执行teardown
    print("第一个用例执行")
    st = 'huace'
    assert 'h' in st


def test_two():              # 执行这个函数前先执行setup  之后再执行teardown
    print('第二个用例执行')
    x = 'xiao'
    assert 'x' in x


if __name__ == '__main__':
    pytest.main(['-vs'])