#!/usr/bin/env python3
class Solution:
    def is_palin(self,s,l,r):
        while l >=0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l+1:r]

    def longestPalin(self, S):
        longest = ""
        for i in range(len(S)):
            # for off case
            tmp = self.is_palin(S,i,i)
            if len(tmp) > len(longest):
                print(tmp, "In odd")
                longest = tmp

            tmp = self.is_palin(S,i,i+1)
            if len(tmp) > len(longest):
                print(tmp, "In even")
                longest = tmp

        return longest

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
