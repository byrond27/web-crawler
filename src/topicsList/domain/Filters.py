class Filters:
    def __init__(self):
        pass

    @staticmethod
    def filterMoreThanFiveWords(topics):
        filteredTopics = []
        for topic in topics:
            if len(topic.title.split()) > 5:
                filteredTopics.append(topic)
        return filteredTopics

    @staticmethod
    def filterMoreLessAndEqualFiveWords(topics):
        filteredTopics = []
        for topic in topics:
            if len(topic.title.split()) <= 5:
                filteredTopics.append(topic)
        return filteredTopics
