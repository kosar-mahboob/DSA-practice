class Solution:
    def minFinishTime(self,
                      landStartTime: List[int],
                      landDuration: List[int],
                      waterStartTime: List[int],
                      waterDuration: List[int]) -> int:
        n = len(landStartTime)
        m = len(waterStartTime)
        best = float('inf')
        for i in range(n):
            land_start = landStartTime[i]
            land_end = land_start + landDuration[i]
            for j in range(m):
                water_start = waterStartTime[j]
                water_end = water_start + waterDuration[j]
                # Order: land then water
                finish_land_then_water = max(water_start, land_end) + waterDuration[j]
                # Order: water then land
                finish_water_then_land = max(land_start, water_end) + landDuration[i]
                best = min(best, finish_land_then_water, finish_water_then_land)
        return best
