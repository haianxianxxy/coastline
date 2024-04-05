import  pytest


@pytest.fixture()
def login():
    print("登录成功")
def test_1(login):
    print('执行完fixture的login后再执行我test1')
def test_2():
    print('不用执行login，直接执行我test2')
def test_3(login):
    print('执行完fixture的login后再执行我test3')


if __name__ == '__main__':
    pytest.main(['-vs', '--ff',  '--html=report.html'])