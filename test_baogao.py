import  pytest
import  time
from selenium import webdriver

def test_bg(browser):
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com/')
    time.sleep(3)
    t = driver.title
    assert '百度' in t



if __name__ == '--main--':
    pytest.main(['-vs', '--html=report.html'])