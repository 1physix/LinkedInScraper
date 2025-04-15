import requests
from bs4 import BeautifulSoup

"""
Three steps:
1. Access the page
2. Break the page down
3. Find the data you want
"""



#Accessing the page:
url = "https://www.linkedin.com/in/ishaqhussain1/"
response = requests.get(url)
html = response.text

#Breaking the HTML down into components (parsing):
soup = BeautifulSoup(html, "html.parser")
image = soup.find("src", id = "ember719")

print(image)
