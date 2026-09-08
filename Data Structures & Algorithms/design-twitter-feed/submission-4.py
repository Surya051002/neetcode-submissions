class Twitter:

    def __init__(self):
        self.tweet=deque()
        self.followers={}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet.append([userId,tweetId])
        if userId not in self.followers:
            self.followers[userId]=[userId]
        # print(self.tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        if userId not in self.followers:
            return []
        followers=self.followers[userId]
        for i in range(len(self.tweet)-1,-1,-1):
            if self.tweet[i][0] in followers:
                res.append(self.tweet[i][1])
            if len(res)==10:
                return res
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            if followeeId not in self.followers[followerId]:
                self.followers[followerId].append(followeeId)
        else:
            self.followers[followerId]=[followerId,followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)
        # print(self.followers)

