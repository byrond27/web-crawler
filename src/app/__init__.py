import requests
import re

from bs4 import BeautifulSoup

from src.modules.domain.Topic import Topic

URL = 'https://news.ycombinator.com/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find("table", class_="itemlist")

job_elems = results.find_all('tr')
topicsArray = []
limitOfEntries = 10;
entriesCounter = 0

for job_elem in job_elems:
    if job_elem.get("id") is not None:
        topicId = job_elem.get("id")
        topic = soup.find(id=topicId)
        title = topic.find(class_="storylink").getText()
        rank = topic.find("span", class_="rank").getText().replace(".", "")
        points = soup.find(id="score_" + topicId).getText().replace(" points", '')
        comments = soup.find("a", href="item?id=" + topicId, text=re.compile('comment'))
        if comments is None:
            comments = "0"
        else:
            comments = comments.getText().split()
            comments = comments[0]
        topic = Topic(topicId, title, rank, points, comments)
        topicsArray.append(topic)
        var = ++entriesCounter
        if entriesCounter == limitOfEntries:
            break

for topic in topicsArray:
    topic.print()

print(len(topicsArray))
