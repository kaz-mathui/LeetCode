class Solution:
    def groupThePeople(self, groupSizes):
        ans,group,next_group = [],[],[]
        for i,j in enumerate(groupSizes):
            print(i,j)
            group.append((j,i))
        group.sort()
        print(group)
        for length,index in group:
            next_group.append(index)
            if len(next_group) == length:
                ans.append(next_group)
                next_group = []    
        return ans
