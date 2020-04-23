class Topic:
    def __init__(self, topicId, title, rank, points, comments):
        self.topicId = topicId
        self.title = title
        self.rank = int(rank)
        self.points = int(points)
        self.comments = int(comments)

    def print(self):
        print("id: ", self.topicId, " title: ", self.title, " rank: ", self.rank, " points: ", self.points,
              " comments: ", self.comments)
