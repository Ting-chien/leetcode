import heapq
from typing import List
from collections import defaultdict

class Twitter:
    """
    Define three dict to store relationship 
    1. user to feeds
    2. user to users they follow
    3. user to users that follow him/her
    their Where feed is a tuple with userId and feedId, and follower is a userId.

    For example

        user_2_feeds = {
            1: [(1, 1001), (2, 1002), (2, 1003)],
            2: [(3, 1004), (2, 1005)]
        }

        user_2_followers = {
            1: [2], 
            2: [3]
        }

        user_2_followees = {
            2: [1],
            3: [2]
        }

    Case 1: When a user sent a post
    1. Find followees in user_2_followees
    2. Add feed to those followees and himself in user_2_feeds

    Case 2: Follow
    1. Add follower and followee relation to user_2_followers
    and user_2_followees

    Case 3: Unfollow
    1. Remove follower and followee relation in user_2_followers
    and user_2_followees
    2. Remove posts written by the followee in the follower's feed list

    Case 4: Get feeds
    1. Get feed by user_id in user_2_feeds
    """

    def __init__(self):
        self._id = 0
        self.feeds = []
        self.user_2_feeds = defaultdict(list)
        self.user_2_followers = defaultdict(set)
        self.user_2_followees = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        # Get followees
        followees = self.user_2_followees[userId]

        # Add post to those followees and the person who tweet
        for _id in list(followees)+[userId]:
            self.user_2_feeds[_id].append((userId, tweetId, self._id))

        # Collect all posts
        self.feeds.append((userId, tweetId, self._id))

        # Auto increase _id
        self._id += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        # Get last 10 posts
        feeds = sorted(self.user_2_feeds[userId], key=lambda x: x[2], reverse=True)[:10]

        # Retrun tweetId only
        return [f[1] for f in feeds]
        

    def follow(self, followerId: int, followeeId: int) -> None:

        # Add posts of followee to follower if new followee
        if followeeId not in self.user_2_followers[followerId]:
            feeds = [f for f in self.feeds if f[0] == followeeId]
            self.user_2_feeds[followerId] += feeds

        # Add relation to follower and followee
        self.user_2_followers[followerId].add(followeeId)
        self.user_2_followees[followeeId].add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        # Remove relation from follower and followee
        # print(id(self.user_2_followers[followerId]))
        # self.safe_remove(self.user_2_followers[followerId], followeeId)
        # self.safe_remove(self.user_2_followees[followeeId], followerId)
        self.user_2_followers[followerId].discard(followeeId)
        self.user_2_followees[followeeId].discard(followerId)

        # Remove post from unfollowee
        self.user_2_feeds[followerId] = [f for f in self.user_2_feeds[followerId] if f[0] != followeeId]



class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> [(time, tweetId)]
        self.following = defaultdict(set)    # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Store tweet once
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1   # decreasing makes heap a max-heap by time

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        # User follows themselves
        users = self.following[userId] | {userId}

        for u in users:
            if self.tweets[u]:
                time, tweetId = self.tweets[u][-1]
                idx = len(self.tweets[u]) - 1
                # (time, tweetId, user, index)
                heap.append((time, tweetId, u, idx))

        heapq.heapify(heap)

        result = []

        while heap and len(result) < 10:
            time, tweetId, u, idx = heapq.heappop(heap)
            result.append(tweetId)

            # Push next older tweet from same user
            if idx > 0:
                next_time, next_tweetId = self.tweets[u][idx - 1]
                heapq.heappush(
                    heap,
                    (next_time, next_tweetId, u, idx - 1)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

        
        


# Your Twitter object will be instantiated and called as such:

def run(ops: List[str], params: List[List[int]]):

    res = []
    twitter = None
    for op, param in zip(ops, params):
        print(f"Running op={op}, param={param}")
        output = None
        if op == "Twitter":
            twitter = Twitter()
        elif op == "postTweet":
            twitter.postTweet(param[0], param[1])
        elif op == "getNewsFeed":
            output = twitter.getNewsFeed(param[0])
        elif op == "follow":
            twitter.follow(param[0], param[1])
        elif op == "unfollow":
            twitter.unfollow(param[0], param[1])

        res.append(output)
        if output:
            output = None

    print(twitter.user_2_feeds)
    print(twitter.user_2_followers)
    print(twitter.user_2_followees)
    print(f"Result: {res}")


# Case 1
ops = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
params = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
run(ops, params)

# Case 2
ops = ["Twitter","postTweet","getNewsFeed","follow","getNewsFeed","unfollow","getNewsFeed"]
params = [[],[1,1],[1],[2,1],[2],[2,1],[2]]
run(ops, params)

# Case 3
ops = ["Twitter","postTweet","follow","follow","getNewsFeed"]
params = [[],[2,5],[1,2],[1,2],[1]]
run(ops, params)
