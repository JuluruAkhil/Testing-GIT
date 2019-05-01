from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
import csv
import re

csv_file = open('Zomato.csv', 'w', encoding='utf-8-sig')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Restaurant Name', 'Area', 'Address', 'Rating', 'Number Of Votes', 'Cuisines', 'Cost For Two', 'Hours', 'Phone No'])

def get_data(i):
    driver = webdriver.Chrome(executable_path = 'D:\\Python\\chromedriver')
    page = 'https://www.zomato.com/hyderabad/best-restaurants?page={}' .format(i)
    driver.get(page)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    driver.quit()
    return soup


for i in range(1,446):
    web = get_data(i)
    for card in web.find_all('div', class_='search-snippet-card'):
        name_card = card.find('a', class_='result-title').text
        area = card.find('a', class_='ln24 search-page-text mr10 zblack search_result_subzone left').text
        address = card.find('div', class_='search-result-address').text
        rating = card.find('div', class_='rating-popup').text
        cuisines = card.find('span', class_='col-s-11 col-m-12 nowrap  pl0')
        cost = card.find('span', class_='col-s-11 col-m-12 pl0').text
        hours_open = card.find('div', class_='col-s-11 col-m-12 pl0 search-grid-right-text ').text
        try:
            phone_no = card.find('a', class_='item res-snippet-ph-info')['data-phone-no-str']
        except Exception as e:
            phone_no = NaN
        # try:
            # votes = card.find('span', class_='rating-votes-div-18280307 grey-text fontsize5').text
        votes = card.select("span.rating-votes")
        # except Exception as e:
        #     votes = 0
        csv_writer.writerow([name_card, area, address, rating, votes, cuisines, cost, hours_open, phone_no])
    print(i)
    print(votes)
csv_file.close()

