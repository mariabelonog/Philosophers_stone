def syn_parcing(word):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    browser = webdriver.Chrome("/Users/mariabelonog/Desktop/chromedriver")
    un = 'https://sinonim.org/s/' + word
    browser.get(un)
    a = browser.find_elements(By.CLASS_NAME, 'nach')
    s = []
    for i in a:
        if i.text.isalpha():
            s.append(i.text.strip())
    return s


"""
для алгоритма был необхалди парсинг синононимов со специальоного сайта
"""