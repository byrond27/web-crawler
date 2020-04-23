class Sorter:
    def __init__(self):
        pass

    @staticmethod
    def sortedByComments(topics):
        return sorted(topics, key=lambda x: x.comments, reverse=True)

    @staticmethod
    def sortedByPoints(topics):
        return sorted(topics, key=lambda x: x.points, reverse=True)