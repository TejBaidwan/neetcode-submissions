class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        total_wait = 0
        finish_time = 0

        for arrival, duration in customers:
            start_time = max(arrival, finish_time)
            finish_time = start_time + duration

            total_wait += finish_time - arrival

        return total_wait / len(customers)
