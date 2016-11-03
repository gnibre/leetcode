import random

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        random.randint(1, 20)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """

        count = self.data.get(val, 0)
        self.data[val] = count + 1
        return count == 0

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        count = self.data.get(val, 0)
        self.data[val] = count - 1 if count > 0 else 0
        return count > 0

    def getRandom(self):
        totalc = sum(self.data.itervalues())
        # waht ever order iter map present, we are doing a 'random' here, so it's equal opportunity for each.
        if totalc == 0:
            return None
        r = random.randint(1,totalc)
        for d,c in self.data.iteritems():
            if c>=r:
                return d
            r-=c
        return d

    def getRandom_On(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        print " get random -> %r "%self.data
        total_seen = 0
        choosen = 0
        for d, c in self.data.iteritems():
            total_seen += c
            # chance of d:  c/total
            if self.roll_dice(c, total_seen):
                choosen = d
        return d

    def roll_dice(self, acc, total):
        #  random in [1,total]
        # if random_res <= acc, return True, which means hit.
        r = random.randint(1, total)
        return r <= acc


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

s = RandomizedCollection()
["RandomizedCollection","insert","remove","insert","getRandom","remove","insert","getRandom"]
[[],[1],[2],[2],[],[1],[2],[]]
print s.insert(1)
print s.remove(2)
print s.insert(2)
print s.getRandom()
print s.remove(1)
print s.insert(2)
print s.getRandom()