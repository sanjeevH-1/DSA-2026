class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap=defaultdict(int)
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hmap:
                return [hmap[complement] , i]

            else:
                hmap[nums[i]] = i




        