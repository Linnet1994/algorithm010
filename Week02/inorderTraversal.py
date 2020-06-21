# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 15:38:26 2020

@author: 50615
"""

class TreeNode():
    def __init(self,x):
        self.val = x
        self.left, self.right = None, None

class solution():
    def inorderTravelsal(self,root):
        res = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res