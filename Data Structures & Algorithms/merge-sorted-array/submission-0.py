class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        S: O(1) - I'm not using additional data structures
        T: O(n + m) where m is the length of list 1 and n is the length of list2
        have three pointers
        p for position
        and p1 and p2 for each list
        loop through p1 and p2 and if p1 < p2 set that at the position and vice versas
        if there are more elements in p2 than add them to nums 1. don't need ot add additonal elements to nums 1 because they are all ready there
        """
        p = len(nums1) - 1 
        p1 = m - 1
        p2 = n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1

        return nums1

        