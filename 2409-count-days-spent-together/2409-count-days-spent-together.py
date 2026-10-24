class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def to_day(date: str) -> int:
            m, d = map(int, date.split('-'))
            return sum(days[:m-1]) + d
        
        a_start = to_day(arriveAlice)
        a_end = to_day(leaveAlice)
        b_start = to_day(arriveBob)
        b_end = to_day(leaveBob)
        
        overlap_start = max(a_start, b_start)
        overlap_end = min(a_end, b_end)
        
        return max(0, overlap_end - overlap_start + 1)