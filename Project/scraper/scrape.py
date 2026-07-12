import requests
from bs4 import BeautifulSoup

url = "https://python.langchain.com/docs/introduction/"

response = requests.get(url)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text()

with open("data/raw_text.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Data scraped successfully!")
