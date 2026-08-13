class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordDict = {}
        
        for word in strs:
            sort = ''.join(sorted(word))

            if sort not in wordDict:
                wordDict[sort] = []

            wordDict[sort].append(word)

        return list(wordDict.values())
