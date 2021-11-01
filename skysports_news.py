import requests
from bs4 import BeautifulSoup

class news():
    
    def webscrape_site(self, url):
        #Returns scraped site
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    
    def get_amount_articles(self, soup, find_class):
        #Get the amount of news articles
        amount_articles = len(soup.find_all("a", class_=find_class))
        return amount_articles
    
    
    def get_news_headers(self, soup, find_class, amount_articles=0):
        #Get news headers and link
        if amount_articles == 0:
            news_header_link = soup.find_all("a", class_=find_class)[0]['href']
            news_class = str(soup.findAll('a', {'class': find_class})[0])
            news_header_start = news_class.find('>') + 1
            news_header_end = news_class.find('</a')
            news_header = news_class[news_header_start:news_header_end].strip()
            return news_header, news_header_link
        else:
            news_items = {}
            for i in range(amount_articles):
                news_header_link = soup.find_all("a", class_=find_class)[i]['href']
                news_class = str(soup.findAll('a', {'class': find_class})[i])
                news_header_start = news_class.find('>') + 1
                news_header_end = news_class.find('</a')
                news_header = news_class[news_header_start:news_header_end].strip()
                news_items[i] = news_header, news_header_link
        return news_items
    
    def get_images(self, soup):
        #Get images from articles
        images = soup.find_all('img')
        all_images = {}
        counter = 0
        for item in images:
            all_images[str(counter)] = item['src']
            counter += 1
        clean_images = {k: v for k, v in   all_images.items() if v != '/core/img/s.png'}
        return clean_images