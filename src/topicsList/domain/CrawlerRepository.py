import abc


class crawlerRepository(abc.ABC):

    @abc.abstractmethod
    def getTopics(self) -> list:
        pass

    @abc.abstractmethod
    def getRequest(self):
        pass

    @abc.abstractmethod
    def getTitle(self, topic):
        pass

    @abc.abstractmethod
    def getRank(self, topic):
        pass

    @abc.abstractmethod
    def getPoints(self, soup, topicId):
        pass

    @abc.abstractmethod
    def getComments(self, soup, topicId):
        pass
