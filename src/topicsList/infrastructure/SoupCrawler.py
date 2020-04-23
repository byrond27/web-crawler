import re

import requests
from bs4 import BeautifulSoup

from src.topic.domain.Topic import Topic
from src.topicsList.domain.CrawlerRepository import crawlerRepository


class soupCrawler(crawlerRepository):
    def __init__(self):
        self.limitOfEntries = 10;
        self.URL = 'https://news.ycombinator.com/'
        pass

    @property
    def getTopics(self):

        page = self.getRequest()

        soup = BeautifulSoup(page.content, 'html.parser')
        tableTopics = soup.find("table", class_="itemlist")
        rows = tableTopics.find_all('tr')
        topics = []
        entriesCounter = 0

        for job_elem in rows:
            if job_elem.get("id") is not None:
                topicId = job_elem.get("id")
                topic = soup.find(id=topicId)
                topic = Topic(topicId, self.getTitle(topic), self.getRank(topic), self.getPoints(soup, topicId), self.getComments(soup, topicId))
                topics.append(topic)
                entriesCounter = entriesCounter + 1
                if entriesCounter == self.limitOfEntries:
                    break
        return topics

    def getRequest(self):
        return requests.get(self.URL)

    def getTitle(self, topic):
        return topic.find(class_="storylink").getText()

    def getRank(self, topic):
        return topic.find("span", class_="rank").getText().replace(".", "")

    def getPoints(self, soup, topicId):
        return soup.find(id="score_" + topicId).getText().replace(" points", '')

    def getComments(self, soup, topicId):
        comments = soup.find("a", href="item?id=" + topicId, text=re.compile('comment'))
        if comments is None:
            return "0"
        comments = comments.getText().split()
        comments = comments[0]
        return comments
