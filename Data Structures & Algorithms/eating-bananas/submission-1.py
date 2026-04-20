class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # T: O(log n)
        # S: O(1)

        #left = 1
        #right = max of any pile
        #loop
        # calculates the mid
        # total hours for the mid
        # total hours is less than hours  move left setting right to mi
        # if total hours is more than move right set left to mid +1 
        # return right which will be the min to eat all bananas

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right)//2

            total_hours = sum(math.ceil(p/mid) for p in piles)

            if total_hours <= h:
                right = mid
            else:
                left = mid + 1
        

        return right