#!/usr/bin/env python3
class Solution:
    def is_palin(self,S,lo,hi,cache):
        if cache[lo][hi] is not None:
            return cache[lo][hi]
        elif lo == hi:
            return True
        elif lo+1 == hi:
            return S[lo] == S[hi]

        ans = False if S[lo] != S[hi] else self.is_palin(S,lo+1,hi-1,cache)
        cache[lo][hi] = ans
        return ans

    def longestPalin(self, S):
        cache = [[None] * len(S) for _ in range(len(S))]
        for l in range(len(S),0,-1):
            for s in range(len(S) - l +1):
                if self.is_palin(S,s,s+l-1,cache):
                    return S[s:s+l]

        return S[0]

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
