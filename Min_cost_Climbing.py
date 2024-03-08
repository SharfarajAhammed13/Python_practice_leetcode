class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) -3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])
    
# Append a 0 to the end of the cost list. This is done to handle the case when there are no more stairs to climb.

# Iterate through the cost list in reverse order, starting from the second-to-last element (len(cost) - 3) and going backwards (-1 step each time).

# For each element, add the minimum cost between the next two steps (cost[i+1] and cost[i+2]) to the current element (cost[i]).

# Finally, return the minimum cost between the first two steps (cost[0] and cost[1]).