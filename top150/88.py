# Date: 2023/11/28
# Time: 3:20
# Difficulty: Easy
# Link: https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

class Solution:

    def order(self, list_to_order: list[int], len: int) -> None:
        # simple sorting
        i=0
        while(i<len-1):
            if(list_to_order[i]>list_to_order[i+1]):
                temp = list_to_order[i]
                list_to_order[i] = list_to_order[i+1]
                list_to_order[i+1] = temp
            i=i+1

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # first merge the two array
        j=0
        for i in range(n):
            nums1[i+m] = nums2[i]
            #nums1[i+(m-1)] = nums2[i]
        
        # now sort  in non-decreasing order 
        self.order(nums1, m+n)

    # to order a single array    
    

# main
obj = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n=3
obj.merge(nums1, m, nums2, n)
print(nums1)