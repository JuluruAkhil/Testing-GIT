from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('restaurants.csv', 'w', encoding='utf-8-sig')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Restaurant Name', 'Rating', 'Price'])

source = requests.get('https://www.dineout.co.in/hyderabad-restaurants', timeout = None).text

soup = BeautifulSoup(source, 'lxml')

for card in soup.find_all('div', class_='listing-card-wrap'):
	
	restaurant_name_class = card.find('a', class_='titleDiv')
	restaurant_name = card.h4.a.text
	
	rating_class = card.find('div', class_='rating')
	rating = rating_class.a.span.text
	
	price = card.find('span', class_='highlight-txt price').text

	print(restaurant_name)
	print(rating)
	print(price)

	csv_writer.writerow([restaurant_name, rating, price])
csv_file.close()
