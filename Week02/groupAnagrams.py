# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 11:35:22 2020

@author: 50615
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for item in strs:
            key = tuple(sorted(item))
            dic[key] = dic.get(key, []) + [item]
        return list(dic.values())
    
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))