from src.topic.domain.Topic import Topic
from src.topicsList.domain.Filters import Filters
from src.topicsList.domain.Sorter import Sorter
import unittest
import requests


class MyTestCase(unittest.TestCase):
    URL = 'https://news.ycombinator.com/'
    topicList = [
        Topic("123", "Lorem ipsum dolor sit amet, consectetur adipiscing elit", "1", "1", "1000"),
        Topic("456", "quis nostrud exercitation ullamco", "2", "500", "200"),
        Topic("789", "quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo", "3", "0", "55"),
        Topic("321", "Nemo enim ipsam voluptatem quia", "4", "321", "0"),
        Topic("159", "Nemo enim", "5", "22", "23")
    ]
    customSorter = Sorter()
    customFilter = Filters()

    def test_should_status_code_200(self):
        page = requests.get(self.URL)
        self.assertEqual(page.status_code, 200)

    def test_should_sort_list_by_comments(self):
        expectList = [
            Topic("123", "Lorem ipsum dolor sit amet, consectetur adipiscing elit", "1", "1", "1000"),
            Topic("456", "quis nostrud exercitation ullamco", "2", "500", "200"),
            Topic("789", "quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo", "3", "0", "55"),
            Topic("159", "Nemo enim", "5", "22", "23"),
            Topic("321", "Nemo enim ipsam voluptatem quia", "4", "321", "0")
        ]
        actualList = self.customSorter.sortedByComments(self.topicList)
        self.assertEqual(list(map(vars, actualList)), list(map(vars, expectList)))

    def test_should_sort_list_by_points(self):

        expectList = [
            Topic("456", "quis nostrud exercitation ullamco", "2", "500", "200"),
            Topic("321", "Nemo enim ipsam voluptatem quia", "4", "321", "0"),
            Topic("159", "Nemo enim", "5", "22", "23"),
            Topic("123", "Lorem ipsum dolor sit amet, consectetur adipiscing elit", "1", "1", "1000"),
            Topic("789", "quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo", "3", "0", "55")
        ]
        actualList = self.customSorter.sortedByPoints(self.topicList)
        self.assertEqual(list(map(vars, actualList)), list(map(vars, expectList)))

    def test_should_return_titles_with_more_than_5_words(self):

        expectList = [
            Topic("123", "Lorem ipsum dolor sit amet, consectetur adipiscing elit", "1", "1", "1000"),
            Topic("789", "quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo", "3", "0", "55")
        ]
        actualList = self.customFilter.filterMoreThanFiveWords(self.topicList)
        self.assertEqual(list(map(vars, actualList)), list(map(vars, expectList)))

    def test_should_return_titles_with_less_or_equal_to_5_words(self):

        expectList = [
            Topic("456", "quis nostrud exercitation ullamco", "2", "500", "200"),
            Topic("321", "Nemo enim ipsam voluptatem quia", "4", "321", "0"),
            Topic("159", "Nemo enim", "5", "22", "23"),
        ]
        actualList = self.customFilter.filterMoreLessAndEqualFiveWords(self.topicList)
        self.assertEqual(list(map(vars, actualList)), list(map(vars, expectList)))

    def test_should_return_titles_with_more_than_5_words_sorted_by_comments(self):

        expectList = [
            Topic("123", "Lorem ipsum dolor sit amet, consectetur adipiscing elit", "1", "1", "1000"),
            Topic("789", "quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo", "3", "0", "55")
        ]
        actualList = self.customSorter.sortedByComments(self.customFilter.filterMoreThanFiveWords(self.topicList))
        self.assertEqual(list(map(vars, actualList)), list(map(vars, expectList)))

    def test_should_return_titles_with_less_or_equal_to_5_words_sorted_by_points(self):

        expectList = [
            Topic("456", "quis nostrud exercitation ullamco", "2", "500", "200"),
            Topic("321", "Nemo enim ipsam voluptatem quia", "4", "321", "0"),
            Topic("159", "Nemo enim", "5", "22", "23"),
        ]
        actualList = self.customSorter.sortedByPoints(self.customFilter.filterMoreLessAndEqualFiveWords(self.topicList))
        self.assertEqual(list(map(vars,actualList)), list(map(vars, expectList)))


if __name__ == '__main__':
    unittest.main()
