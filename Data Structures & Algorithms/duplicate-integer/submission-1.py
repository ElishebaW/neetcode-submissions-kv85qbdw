class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        unique = set()

        for num in nums:
            if num in unique:
                return True
            unique.add(num)

        return False


    """ 
    t: O(n)
    s: O(n)

    # loop through nums
    # if that num is in hashmap
    # then the array contains a duplica
    # if not, add that num to the hash map/ set
    # return false
    """