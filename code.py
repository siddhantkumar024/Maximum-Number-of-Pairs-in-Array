class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d={}
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        print(d)
        cp=0
        r=0
        for k,v in d.items():
            cp+=(v//2)
            r+=(v%2)
        return [cp,r]

        
