class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        remaining = [] #--- indices
        for i in range(0, n):
            while remaining and temperatures[i] > temperatures[remaining[-1]]:
                    ind = remaining.pop()
                    res[ind] = i - ind
            if i == n - 1:
                return res
            elif temperatures[i + 1] > temperatures[i]:
                res[i] = 1
            else:
                remaining.append(i)
        return res
            

        # min_days = 0
        # n = len(temperatures)
        # after = [0] * n
        # for i in range(n - 2, -1, -1):
        #     if temperatures[i+1] > temperatures[i]:
        #         after[i] = 1
        #     elif after[i + 1] == 0:
        #         after[i] = 0
        #     else:
        #         # see how many days the i + 1 has to wait, i has to wait that many days + 1 for sure
        #         min_days = after[i + 1] + 1
        #         # now, 69 had to wait 1 day and the element at that day is 72, so we are done.
        #         # oh so we have to keep adding like this until the day has higher value than curr

        #         #---- check the index calculations thoroughly ----
        #         pointer = i + min_days #-- 2 + 2 + 1 = 5
        #         while temperatures[pointer] <= temperatures[i]:
        #             if pointer >= n - 1 or after[pointer]  == 0:
        #                 min_days = 0
        #                 break
        #             min_days += after[pointer] # 8 - 5 - 1 = 2 val = 1
        #             pointer += after[pointer] # 6
        #         after[i] = min_days
    
        # return after


            