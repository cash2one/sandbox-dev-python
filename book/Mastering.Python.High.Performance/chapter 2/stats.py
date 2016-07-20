import sys

class TwittStats:
    STATS_FILE = './files/tweets.csv'

    def __init__(self):
        self.replies = 0
        self.from_web = 0
        self.from_phone = 0
        self.lines_parts = []
        self.total_tweets = 0


    def getPercentage(self, n, total):
        return (n * 100) / total

    def read_data(self):
        f = open(TwittStats.STATS_FILE, 'r')

        lines = f.read().strip().split("\"\n\"")
        for line in lines:
           self.total_tweets += 1
           self.lines_parts.append(line.strip().split(',')) 
        return self

    def incStat(self, st):
        setattr(self,st, getattr(self, st) + 1)

    def get_stats(self):
        for i in self.lines_parts:
            if(i[1] != '""'):
                self.incStat('replies')
            if(i[4].find('Twitter Web Client') > -1):
                self.incStat('from_web')
            else:
                self.incStat('from_phone')

        return self

    def print_results(self):
        print "-------- My twitter stats -------------"
        print "%s%% of tweets are replies" % (self.getPercentage(self.replies, self.total_tweets))
        print "%s%% of tweets were made from the website" % (self.getPercentage(self.from_web, self.total_tweets))
        print "%s%% of tweets were made from my phone" % (self.getPercentage(self.from_phone, self.total_tweets))