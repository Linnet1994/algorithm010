# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 11:28:41 2020

@author: 50615
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        se = set(s)
        if se == set(t):
            for i in se:
                if s.count(i) != t.count(i):
                    return False
            return  True
        else:
            return False
