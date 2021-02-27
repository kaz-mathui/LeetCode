class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        def numberOfDaysNeededWithCapacity(weights: List[int],mid:int) -> int:
            daysRequired = 1
            curr = 0
            
            for w in weights:
                curr += w
                if curr > mid:
                    daysRequired += 1
                    curr = w
            return daysRequired
        
        bottom = max(weights)
        top = sum(weights)
        ans = 0
        while bottom < top:
            mid = (bottom + top)//2
            days = numberOfDaysNeededWithCapacity(weights,mid)
            curr_weight = 0
            
            if days > D:
                bottom = mid + 1
            else:
                top = mid

        return top
        
        