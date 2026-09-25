from collections import defaultdict
import heapq


class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)

    def getNewsFeed(self, userId: int) -> List[int]:

        heap = []
        result = []

        users = self.followMap[userId].copy()
        users.add(userId)

        # Put the newest tweet from every user into the heap.
        for user in users:

            tweets = self.tweetMap[user]

            if not tweets:
                continue

            index = len(tweets) - 1
            time, tweetId = tweets[index]

            heapq.heappush(
                heap,
                (-time, tweetId, user, index - 1)
            )

        # Get the 10 newest tweets.
        while heap and len(result) < 10:

            _, tweetId, user, index = heapq.heappop(heap)

            result.append(tweetId)

            # Add this user's next newest tweet.
            if index >= 0:

                time, tweetId = self.tweetMap[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index - 1)
                )

        return result
        