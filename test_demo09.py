import  pytest

# 此处两个方法调用了conftest.py里边的装饰的login函数

def test_1():
    print('执行test1')


@pytest.mark.baidu   #mark标记  只执行标记的函数
def test_baidu():
    print('执行百度')

@pytest.mark.biying
def test_biying():
    print('执行必应')


if __name__ == '__main__':
    pytest.main(['-vs'])