class TopicsList:
    def __init__(self, topics):
        self.topics = topics

    def printList(self):
        for topic in self.topics:
            topic.print()
