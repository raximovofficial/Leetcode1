class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        c=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i]==words[j][::-1]:
                    c+=1
        return c

a = Solution()
print(a.maximumNumberOfStringPairs(words = ["cd","ac","dc","ca","zz"]))