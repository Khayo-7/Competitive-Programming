class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        store = {}

        for i in range(len(nums)):
            store[nums[i]] = i

        for operation in operations:
            store[operation[1]] = store[operation[0]]
            store.pop(operation[0])
        
        for key, index in store.items():
            nums[index] = key
        
        return nums

        # for operation in operations:
        #     index = nums.index(operation[0])
        #     nums[index] = operation[1]

        # return nums
        
        