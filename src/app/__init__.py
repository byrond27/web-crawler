from src.modules.topicsList.application.Crawler import Crawler
from src.modules.topicsList.domain.TopicsList import TopicsList


def Main():
    crawler = Crawler()
    topics = crawler.getTopics()
    TopicsList(topics).printList()
    print("More")
    ListMoreThanFiveWords = crawler.sortedByComments(crawler.filterMoreThanFiveWords(topics))
    TopicsList(ListMoreThanFiveWords).printList()
    print("Less")
    ArrayLessAndEqualThanFiveWords = crawler.sortedByPoints(crawler.filterMoreLessAndEqualFiveWords(topics))
    TopicsList(ArrayLessAndEqualThanFiveWords).printList()


if __name__ == '__main__':
    Main()
