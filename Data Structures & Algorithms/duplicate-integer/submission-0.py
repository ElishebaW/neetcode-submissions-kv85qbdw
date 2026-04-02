class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hash map, if any count is higher than 2 T: O(n)- loop through nums to add to hashmap
        # S: O(n)- hashmap

        #sort and then go through and see if the adjacent one is the same T: O ( n log n) for the sort S
        # S: O(n)

        if (len(nums) == 0):
            return False

        nums_map = {}

        for elem in nums:
            nums_map[elem] = nums_map.get(elem, 0) + 1


        print(f"{nums_map} : The map")

        for count in nums_map.values():
            if count > 1:
                return True


        return False

        