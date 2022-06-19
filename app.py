import requests
from bs4 import BeautifulSoup
response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")
x = soup.select(
    ".s-post-summary.js-post-summary")

for i in x:

    print(i.select_one(".s-post-summary--content>h3>a").text)
    print("\nVotes:"+i.select_one(".s-post-summary--stats.js-post-summary-stats>div>span").text, end="      ")
    print("answers:"+i.select_one(".s-post-summary--stats.js-post-summary-stats>.s-post-summary--stats-item:nth-child(2)>span").text, end="      ")
    print("views:"+i.select_one(".s-post-summary--stats.js-post-summary-stats>.s-post-summary--stats-item:nth-child(3)>span").text, end="\n\n\n")
