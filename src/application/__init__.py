from src.topicsList.domain.Sorter import Sorter
from src.topicsList.infrastructure.SoupCrawler import soupCrawler
from src.topicsList.domain.TopicsList import TopicsList
from src.topicsList.domain.Filters import Filters


def Main():
    crawler = soupCrawler()
    customFilter = Filters()
    sorter = Sorter()
    topics = crawler.getTopics

    print("Original List")
    TopicsList(topics).printList()

    print("List with more then five words in the title and order by Comments")
    ListMoreThanFiveWords = sorter.sortedByComments(customFilter.filterMoreThanFiveWords(topics))
    TopicsList(ListMoreThanFiveWords).printList()

    print("List with less or equal to five words in the title and order by Comments")
    ArrayLessAndEqualThanFiveWords = sorter.sortedByPoints(customFilter.filterMoreLessAndEqualFiveWords(topics))
    TopicsList(ArrayLessAndEqualThanFiveWords).printList()


if __name__ == '__main__':
    Main()
