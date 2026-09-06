class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        sorted_greed = sorted(g)
        sorted_cookies = sorted(s)

        greed = 0
        cookie = 0

        while cookie < len(sorted_cookies) and greed < len(sorted_greed):
            if sorted_cookies[cookie] >= sorted_greed[greed]:
                greed += 1
                cookie += 1
            else:
                cookie += 1
        
        return greed