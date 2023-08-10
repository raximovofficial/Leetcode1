class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        a=zip(heights,names)
        l=[]
        for i,j in sorted(a):
            l.append(j)
        return l[::-1]

a = Solution()
print(a.sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))