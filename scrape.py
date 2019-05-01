from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('tweets.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['tweet_text', 'time'])

source = requests.get('https://twitter.com/realDonaldTrump', timeout = None).text

soup = BeautifulSoup(source, 'lxml')

for tweet in soup.find_all('div', class_="content"):

	tweet_text = tweet.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

	time = tweet.find('a', class_="tweet-timestamp js-permalink js-nav js-tooltip")['title']

	print(time)
	print(tweet_text)
	print()

	csv_writer.writerow([tweet_text, time])

csv_file.close()
