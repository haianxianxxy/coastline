def test_num():
    assert 1 == 2


def aaa():
    assert 3 == 2  # pytest只能识别test开头的方法


def test_aaa():
    assert 2 == 2
