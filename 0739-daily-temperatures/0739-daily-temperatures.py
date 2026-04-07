class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        after = [0]
        min_days = 0
        n = len(temperatures)
        for i in range(n - 2, -1, -1):
            if temperatures[i+1] > temperatures[i]:
                after.append(1)
            elif after[n - i - 2] == 0:
                after.append(0)
            else:
                # see how many days the i + 1 has to wait, i has to wait that many days + 1 for sure
                min_days = after[n - i - 2] + 1
                # now, 69 had to wait 1 day and the element at that day is 72, so we are done.
                # oh so we have to keep adding like this until the day has higher value than curr

                #---- check the index calculations thoroughly ----
                val = temperatures[i + min_days]
                pointer = i + min_days #-- 2 + 2 + 1 = 5
                while val <= temperatures[i]:
                    # print(val, temperatures[i], pointer)
                    if pointer >= n - 1 or after[n - pointer - 1]  == 0:
                        min_days = 0
                        break
                    min_days += after[n - pointer - 1] # 8 - 5 - 1 = 2 val = 1
                    pointer += after[n - pointer - 1] # 6
                    val = temperatures[pointer]
                after.append(min_days)
        after.reverse()
    
        return after


            