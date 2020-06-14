# -*- coding: utf-8 -*-
"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        '''
        # 插入
        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0,nums.pop())
        '''
        
        # 拼接
        
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[0:-k]
        
        # 翻转
        '''
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[0:k] = nums[0:k][::-1]
        nums[k:] = nums[k:][::-1]
        '''