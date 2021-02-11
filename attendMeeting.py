# class Solution:
#     def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
#         attend = []
#         for i in range(len(intervals)):
#             for j in range(intervals[i][0],intervals[i][1]):
#                 if j in attend:
#                     return False
#                 else:    
#                     attend.append(j)
#         return True

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        def overlap(interval1: List[List[int]],interval2: List[List[int]]):
            if (interval1[0] <= interval2[0] and interval1[1] > interval2[0]) or (interval2[0] <= interval1[0] and interval2[1] > interval1[0]):
                return True
            else:
                return False
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if overlap(intervals[i],intervals[j]):
                    return False
                
        return True