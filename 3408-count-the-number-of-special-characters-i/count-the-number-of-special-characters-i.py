class Solution(object):
    def numberOfSpecialChars(self, word):
        low=word.lower()
        uni=set(low)
        count=0
        for i in uni:
            if (i.lower() in word) and (i.upper() in word):
                count+=1
        return count
        