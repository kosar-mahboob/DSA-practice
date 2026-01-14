//leetcode problem no : 3453. Separate Squares I
#include <vector>
#include <algorithm>
#include <cstdint>
using namespace std;

class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        // Step 1: Collect slope change events
        vector<pair<long long, long long>> events;
        long long totalArea = 0;
        
        for (const auto& sq : squares) {
            long long y = sq[1];
            long long l = sq[2];
            totalArea += l * l;
            events.emplace_back(y, l);          // Start of square, slope increases
            events.emplace_back(y + l, -l);     // End of square, slope decreases
        }
        
        // Step 2: Sort events by y-coordinate
        sort(events.begin(), events.end());
        
        // Step 3: Sweep line to find the target height
        double target = totalArea / 2.0;
        double currentArea = 0.0;
        long long currentSlope = 0;
        long long prevY = events[0].first;
        int n = events.size();
        int i = 0;
        
        while (i < n) {
            long long currentY = events[i].first;
            
            // Calculate area in the segment [prevY, currentY]
            if (currentY > prevY) {
                double segmentArea = currentSlope * (currentY - prevY);
                
                // If target is within this segment, interpolate
                if (currentArea + segmentArea >= target - 1e-12) {
                    double needed = target - currentArea;
                    return prevY + needed / currentSlope;
                }
                
                currentArea += segmentArea;
                prevY = currentY;
            }
            
            // Process all events at currentY
            while (i < n && events[i].first == currentY) {
                currentSlope += events[i].second;
                i++;
            }
        }
        
        return prevY; // Should not reach here
    }
};
