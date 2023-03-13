from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
browser = webdriver.Chrome("/Users/mariabelonog/Desktop/chromedriver")
url = 'https://xn--80afcdbalict6afooklqi5o.xn--p1ai/public/application/cards?SearchString=&Statuses%5B0%5D.Selected=true&Statuses%5B0%5D.Name=%D0%BF%D0%BE%D0%B1%D0%B5%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C+%D0%BA%D0%BE%D0%BD%D0%BA%D1%83%D1%80%D1%81%D0%B0&Statuses%5B1%5D.Name=%D0%BD%D0%B0+%D0%BD%D0%B5%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D0%BE%D0%B9+%D1%8D%D0%BA%D1%81%D0%BF%D0%B5%D1%80%D1%82%D0%B8%D0%B7%D0%B5&Statuses%5B2%5D.Name=%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82+%D0%BD%D0%B5+%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D0%BB+%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%BA%D1%83&RegionId=&AreaCityId=&ContestDirectionTenantId=&IsNormalTermProjects=true&IsLongTermProjects=true&CompetitionId=&DateFrom=&DateTo=&Statuses%5B0%5D.Selected=false&Statuses%5B1%5D.Selected=false&Statuses%5B2%5D.Selected=false&IsNormalTermProjects=false&IsLongTermProjects=false'


new = 'new_csv.csv'
with open(new, 'w', newline='') as csvfile:
    writer = csv.writer(
        csvfile, delimiter=';', quotechar='"',
        quoting=csv.QUOTE_MINIMAL)
    row = ['name', 'area']
    writer.writerow(row)

try:
    s = []
    with open(new, 'w', newline='') as csvfile:
        writer = csv.writer(
            csvfile, delimiter='-', quotechar='"',
            quoting=csv.QUOTE_MINIMAL)
        row = ['NAME', 'AREA']
        writer.writerow(row)
        for i in range(1217):
            un = url + '&page=' + str(i)
            browser.get(un)
            a = browser.find_elements(By.CLASS_NAME, 'projects__title')
            b = browser.find_elements(By.CLASS_NAME, 'direction')
            for n in range(20):
                s1 = []
                s1.append(a[n].text)
                s1.append(b[n].text)
                writer.writerow(s1)
except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()