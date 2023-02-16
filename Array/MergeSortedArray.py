from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return
        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return
        nums1_counter = m - 1
        nums2_counter = n - 1
        for i in range(len(nums1) - 1, -1, -1):
            if nums2_counter < 0:
                return
            elif nums1_counter < 0 or nums2[nums2_counter] > nums1[nums1_counter]:
                nums1[i] = nums2[nums2_counter]
                nums2_counter -= 1
            else:
                nums1[i] = nums1[nums1_counter]
                nums1_counter -= 1
        return


solution = Solution()
solution.merge([2, 0], 1, [1], 1)
