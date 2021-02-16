import requests
from bs4 import BeautifulSoup

url = "https://www.linkedin.com/jobs/" 

page = requests.get(url)

content = BeautifulSoup(page.text, 'html.parser')


#get the text
print(content.prettify())


text = content.find_all("a", class_="learning-cta__link")
print(text)