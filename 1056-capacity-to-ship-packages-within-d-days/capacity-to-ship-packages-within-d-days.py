# This function is a feasibility function and this function is the heart of Binary Search On Answer ( BSOA )
# Challenges in Binary Search On Answer ( BSOA )
# 1. Finding the feasibility function.
# 2. converting this brute force approach into binary search on answer and finding low and high
def canShip(weights,days_have,capacity):
    # Find the days_needed to ship all the weights under choosen capacity
    days_needed = 1
    cWeightSum = 0
    for w in weights:
        if cWeightSum + w <= capacity:
            cWeightSum += w
        else:
            days_needed += 1
            cWeightSum = w
    return days_needed <= days_have
    # compare days_needed <= days_have ( capacity is a valid choice )
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # This is the Binary Search On Answer ( BSOA )
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = ( low + high ) // 2
            if canShip(weights, days, mid):
                high = mid
            else:
                low = mid + 1
        return low