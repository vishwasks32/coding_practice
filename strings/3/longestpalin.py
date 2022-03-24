#!/usr/bin/env python3
from itertools import combinations
class Solution:
    def longestPalin(self, S):
        substrs = [S[x:y] for x,y in combinations(range(len(S)+1),2)]
        srtd = sorted(substrs,key=len,reverse=True)
        for item in srtd:
            if item == item[::-1] and len(item) != 1:
                return item

        return S[0]

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
