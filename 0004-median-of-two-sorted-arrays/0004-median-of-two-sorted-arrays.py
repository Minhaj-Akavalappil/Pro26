class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        start, end = 0, m
        
        while start <= end:
            partitionX = (start + end) // 2
            partitionY = (m + n + 1) // 2 - partitionX
            
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Correct partition found
                if (m + n) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                end = partitionX - 1
            else:
                start = partitionX + 1
