class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        hottest = 0

        for i in range(n-1, -1, -1):
            curr_day_temp = temperatures[i]
            if hottest <= curr_day_temp:
                hottest = curr_day_temp
                continue
            
            days = 1
            while temperatures[i + days] <= curr_day_temp:
                days += res[i + days]
            res[i] = days

        return res