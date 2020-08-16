"""
// Time Complexity : o(n)
// Space Complexity : o(n), dictionary
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no


// Your code here along with comments explaining your approach
"""

from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        max_freq = 0
        max_ct = 0
        
        for task in tasks: #for freq of all tasks
            d[task] += 1
            max_freq = max(max_freq, d[task]) #maxfreq value
            
        for k, v in d.items(): #all tasks with max_freq, have to be paired and placed together so getting count
            if d[k] == max_freq:
                max_ct += 1
                
        partitions = max_freq - 1 #number of partitions after placing all the tasks with max_frq
        empty = (n-(max_ct-1)) * partitions #empty spaces
        pending = len(tasks) - max_freq * max_ct #pending tasks
        idle = max(0, empty - pending) #idle spots needed
        
        return idle + len(tasks)
        