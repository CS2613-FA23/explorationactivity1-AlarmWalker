import requests
from bs4 import BeautifulSoup

provinces = ["new-brunswick", "prince-edward-island", "nova-scotia", "newfoundland-labrador"]

news_data = []

#loop through Atlantic provinces
for i in provinces:
    page_url = "https://www.cbc.ca/news/canada/" + i
    response = requests.get(page_url)

    soup = BeautifulSoup(response.text, 'html.parser')

    news_contents = soup.find('div', class_= 'contentArea')
    news_elements = news_contents.find_all('a', class_= 'card')

    for news_element in news_elements:
        news = {}
        news['title'] = news_element.find('h3').text
        description_div = news_element.find('div', class_='description')
        if description_div:
            news['summary'] = description_div.text
        else:
            news['summary'] = "Description not available"
        news['location'] = i

        news_data.append(news)

for news in news_data:
    print(f"Title: {news['title']}")
    print(f"summary: {news['summary']}")
    print(f"location: {news['location']}")
    print()