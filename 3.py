4. Median of Two Sorted Arrays
```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newn=nums1+nums2
        newn.sort()
        length=len(newn)
        index=length//2
        if (length%2)==1:
            return float(newn[index])
        else:
            return float((newn[index]+newn[index-1])/2)
```
