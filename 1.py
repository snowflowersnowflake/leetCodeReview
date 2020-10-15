class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for elei,i in enumerate(nums):
            tmp=target-i
            try:
                elej=nums.index(tmp)
                if(elei!=elej):
                    return [elei,elej]
            except:
                continue
                
                
```python
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```
