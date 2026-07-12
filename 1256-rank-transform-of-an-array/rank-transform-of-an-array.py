class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        arr2 = sorted(set(arr))
        hmap={}
        
        for i , val in enumerate(arr2):
            hmap[val] = 1+i
            
        ans=[]

        for i in arr:
            if i in hmap:
                ans.append(hmap[i])
        return ans



        