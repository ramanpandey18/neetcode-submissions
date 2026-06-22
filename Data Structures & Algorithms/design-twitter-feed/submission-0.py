from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.tweetMap[userId].append(
            (self.time, tweetId)
        )

        self.time += 1

    def follow(self,
               followerId: int,
               followeeId: int) -> None:

        self.followMap[followerId].add(
            followeeId
        )

    def unfollow(self,
                 followerId: int,
                 followeeId: int) -> None:

        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(
                followeeId
            )

    def getNewsFeed(self,
                    userId: int) -> List[int]:

        heap = []
        result = []

        followees = self.followMap[userId].copy()

        followees.add(userId)

        for user in followees:

            tweets = self.tweetMap[user]

            if tweets:

                idx = len(tweets) - 1

                time, tweetId = tweets[idx]

                heapq.heappush(
                    heap,
                    (-time,
                     tweetId,
                     user,
                     idx - 1)
                )

        while heap and len(result) < 10:

            negTime, tweetId, user, idx = \
                heapq.heappop(heap)

            result.append(tweetId)

            if idx >= 0:

                time, tweetId = \
                    self.tweetMap[user][idx]

                heapq.heappush(
                    heap,
                    (-time,
                     tweetId,
                     user,
                     idx - 1)
                )

        return result