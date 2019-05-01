from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

csv_file = open('Zomato.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Restaurants'])
i = 1
driver = webdriver.Chrome(executable_path = 'C:\\Users\\Akhl\\Desktop\\Python\\chromedriver')
page = 'https://www.zomato.com/hyderabad/best-restaurants?page={}' .format(i)
driver.get(page)
# html = driver.page_source
# soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())

    # driver.find_element_by_xpath('//*[@id="mainframe"]/div[2]/div[3]/div[2]/div/div[1]/div[1]/div[10]/a[2]/div/span').click()
    # index = driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="search-results-container"]/div[2]/div[1]/div[2]/div/div/a[3]')))
    # index.click()