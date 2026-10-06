class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.follow_map[userId].copy()
        users.add(userId)
        max_heap = []
        res = []
        for user in users:
            tweets = self.tweet_map[user]
            if not tweets:
                continue
            index = len(tweets) - 1
            time, tweet_id = tweets[index]
            heapq.heappush(max_heap, (-time,tweet_id,user,index - 1))
        
        while max_heap and len(res) < 10:
            time, tweet_id, user, index = heapq.heappop(max_heap)
            res.append(tweet_id)
            if index >= 0:
                time, tweet_id = self.tweet_map[user][index]
                heapq.heappush(max_heap,(-time,tweet_id,user,index-1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
        
