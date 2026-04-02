class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap, count all the elements and return the highests count values
        #hashtable, count all elements and assign them to their respective index and return all the non 0 ones from the back
        #Bucketsort
    #heap

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n , 0) + 1
        
        for num , count in count.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res