class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)
        self.tweets[tweetName].sort()

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.tweets:
            return []
        time = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        n = math.ceil((endTime - startTime + 1) / time)
        counts = [0] * n
        start = bisect_left(self.tweets[tweetName], startTime)
        end = bisect_right(self.tweets[tweetName], endTime, start)
        for i in range(start, end):
            idx = (self.tweets[tweetName][i] - startTime) // time
            counts[idx] += 1
        return counts


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)