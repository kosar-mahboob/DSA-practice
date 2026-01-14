// leetcode problem no : 3454. Separate Squares II
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
using namespace std;

class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        return minYLine(squares);
    }

private:
    double minYLine(vector<vector<int>>& squares) {
        // Step 1: Collect all events
        vector<pair<double, pair<double, double>>> events; // {y, {x, x+l}}
        vector<pair<double, pair<double, double>>> removeEvents; // {y+l, {x, x+l}}
        
        for (auto& sq : squares) {
            double x = sq[0], y = sq[1], l = sq[2];
            events.emplace_back(y, make_pair(x, x + l));
            removeEvents.emplace_back(y + l, make_pair(x, x + l));
        }
        
        // Combine and sort events
        vector<pair<double, int>> allEvents; // {y, index} or {y, -index-1}
        for (int i = 0; i < events.size(); i++) {
            allEvents.emplace_back(events[i].first, i); // start
            allEvents.emplace_back(removeEvents[i].first, -i - 1); // end
        }
        
        sort(allEvents.begin(), allEvents.end());
        
        // Step 2: Sweep line to get bands
        vector<double> bandStarts;
        vector<double> unionLengths;
        
        // Active intervals sorted by x-start
        map<double, double> activeIntervals; // {start, end}
        
        double totalArea = 0.0;
        double prevY = allEvents[0].first;
        
        int eventIdx = 0;
        while (eventIdx < allEvents.size()) {
            double currentY = allEvents[eventIdx].first;
            
            // Add union area for previous band
            if (currentY > prevY) {
                // Calculate union length of active intervals
                double unionLen = 0.0;
                double lastEnd = -1e100;
                
                for (auto& interval : activeIntervals) {
                    double start = interval.first;
                    double end = interval.second;
                    
                    if (start > lastEnd) {
                        unionLen += (end - start);
                        lastEnd = end;
                    } else if (end > lastEnd) {
                        unionLen += (end - lastEnd);
                        lastEnd = end;
                    }
                }
                
                bandStarts.push_back(prevY);
                unionLengths.push_back(unionLen);
                totalArea += unionLen * (currentY - prevY);
            }
            
            // Process all events at currentY
            while (eventIdx < allEvents.size() && 
                   abs(allEvents[eventIdx].first - currentY) < 1e-12) {
                int idx = allEvents[eventIdx].second;
                
                if (idx >= 0) {
                    // Add interval
                    double start = events[idx].second.first;
                    double end = events[idx].second.second;
                    
                    // Insert interval, handle overlaps
                    auto it = activeIntervals.upper_bound(start);
                    if (it != activeIntervals.begin()) {
                        auto prevIt = prev(it);
                        if (prevIt->second >= start) {
                            // Merge with previous
                            start = min(start, prevIt->first);
                            end = max(end, prevIt->second);
                            activeIntervals.erase(prevIt);
                        }
                    }
                    
                    // Merge with overlapping intervals
                    it = activeIntervals.lower_bound(start);
                    while (it != activeIntervals.end() && it->first <= end) {
                        end = max(end, it->second);
                        it = activeIntervals.erase(it);
                    }
                    
                    activeIntervals[start] = end;
                } else {
                    // Remove interval
                    idx = -idx - 1;
                    double start = events[idx].second.first;
                    double end = events[idx].second.second;
                    
                    // Find and remove the interval
                    auto it = activeIntervals.upper_bound(start);
                    if (it != activeIntervals.begin()) {
                        --it;
                        if (it->first <= start && it->second >= end) {
                            // This interval contains the one to remove
                            double oldStart = it->first;
                            double oldEnd = it->second;
                            
                            activeIntervals.erase(it);
                            
                            // Add back the non-overlapping parts
                            if (oldStart < start) {
                                activeIntervals[oldStart] = start;
                            }
                            if (end < oldEnd) {
                                activeIntervals[end] = oldEnd;
                            }
                        }
                    }
                }
                
                eventIdx++;
            }
            
            prevY = currentY;
        }
        
        // Add last band if needed
        if (!activeIntervals.empty() && eventIdx > 0) {
            double unionLen = 0.0;
            double lastEnd = -1e100;
            
            for (auto& interval : activeIntervals) {
                double start = interval.first;
                double end = interval.second;
                
                if (start > lastEnd) {
                    unionLen += (end - start);
                    lastEnd = end;
                } else if (end > lastEnd) {
                    unionLen += (end - lastEnd);
                    lastEnd = end;
                }
            }
            
            // For the last band, we just need it for calculations
        }
        
        // Step 3: Calculate suffix sums
        int numBands = bandStarts.size();
        vector<double> suffixSums(numBands + 1, 0.0);
        
        for (int i = numBands - 1; i >= 0; i--) {
            double yNext = (i + 1 < numBands) ? bandStarts[i + 1] : prevY;
            double bandArea = unionLengths[i] * (yNext - bandStarts[i]);
            suffixSums[i] = bandArea + suffixSums[i + 1];
        }
        
        // Step 4: Find split point
        double target = totalArea / 2.0;
        
        for (int i = 0; i < numBands; i++) {
            double yStart = bandStarts[i];
            double yEnd = (i + 1 < numBands) ? bandStarts[i + 1] : prevY;
            
            if (yEnd <= yStart + 1e-12) continue;
            
            // Calculate area above at yStart and yEnd
            double areaAboveStart = suffixSums[i];  // This includes current band
            double areaAboveEnd = suffixSums[i + 1];
            
            // Check if target is between areaAboveEnd and areaAboveStart
            if (areaAboveEnd <= target + 1e-12 && target <= areaAboveStart + 1e-12) {
                if (abs(areaAboveEnd - target) < 1e-12) {
                    return yEnd;
                }
                
                // Solve for h in this band
                // areaAbove(h) = U_i * (yEnd - h) + S[i+1] = target
                double h = yEnd - (target - suffixSums[i + 1]) / unionLengths[i];
                
                // Make sure h is within [yStart, yEnd]
                if (h < yStart - 1e-12) h = yStart;
                if (h > yEnd + 1e-12) h = yEnd;
                
                return h;
            }
        }
        
        // Special case: line at bottom
        if (abs(suffixSums[0] - target) < 1e-12) {
            return bandStarts.empty() ? 0.0 : bandStarts[0];
        }
        
        // If no split found (shouldn't happen), return 0
        return 0.0;
    }
};

// Test cases can be added here if needed
