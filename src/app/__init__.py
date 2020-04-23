from bs4 import BeautifulSoup
import requests
import re

from src.modules.topic.domain.Topic import Topic
from src.modules.topicsList.domain.TopicsList import TopicsList


def filterMoreThanFiveWords(topics):
    filteredTopics = []
    for topic in topics:
        if len(topic.title.split()) > 5:
            filteredTopics.append(topic)
    return filteredTopics


def filterMoreLessAndEqualFiveWords(topics):
    filteredTopics = []
    for topic in topics:
        if len(topic.title.split()) <= 5:
            filteredTopics.append(topic)
    return filteredTopics


def sortedByComments(topics):
    return sorted(topics, key=lambda x: x.comments, reverse=True)


def sortedByPoints(topics):
    return sorted(topics, key=lambda x: x.points, reverse=True)


def getTopics():
    URL = 'https://news.ycombinator.com/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    tableTopics = soup.find("table", class_="itemlist")

    rows = tableTopics.find_all('tr')
    topicsArray = []
    limitOfEntries = 10;
    entriesCounter = 0

    for job_elem in rows:
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
            entriesCounter = entriesCounter + 1
            if entriesCounter == limitOfEntries:
                break
    return topicsArray


def Main():
    topics = getTopics()
    TopicsList(topics).printList()
    print("More")
    ListMoreThanFiveWords = sortedByComments(filterMoreThanFiveWords(topics))
    TopicsList(ListMoreThanFiveWords).printList()
    print("Less")
    ArrayLessAndEqualThanFiveWords = sortedByPoints(filterMoreLessAndEqualFiveWords(topics))
    TopicsList(ArrayLessAndEqualThanFiveWords).printList()


if __name__ == '__main__':
    Main()
