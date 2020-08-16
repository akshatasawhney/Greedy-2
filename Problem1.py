"""
// Time Complexity : o(n)
// Space Complexity : constant
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no


// Your code here along with comments explaining your approach
"""

class Solution:
    def candy(self, ratings: List[int]) -> int: #2 pass algorithm, first we check going left to right and then right to left
        candies = [1] * len(ratings) #initially everyone has 1 candy
        
        for i in range(1,len(ratings)): #checking with previous values
            if ratings[i] > ratings[i-1]: #if rating for current is higher, increase the number of candies for current to prev candies + 1
                candies[i] = candies[i-1] + 1
                
        for i in range(len(ratings)-2, -1, -1): #2nd pass, 
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i],candies[i+1] + 1) #check if current number of candies is already greater than the right neighbour, else increment by 1
                
        return sum(candies) #return sum 
                
                
            