class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # In backtracking, the standard pattern is to Add -> Recurse -> Remove. You want to modify the same list and clean up after yourself.
        res = []
        def backtrack(lower, curr_sum, curr_combo):
            if len(curr_combo) == k and curr_sum == n:
                res.append(curr_combo[:])
                return
            
            for i in range(lower, 10):
                if curr_sum + i > n:
                    break
                if len(curr_combo) >= k:
                    break
                curr_combo.append(i)
                backtrack(i + 1, curr_sum + i, curr_combo)
                curr_combo.pop()

        backtrack(1, 0, [])
        return res
        # naturally sorted
        # sum3 -> sum2 -> sum1
        # when sum 2 numbers (i,j): if n - sumof2 <= i and j, then invalid, else append[i,j, n - (i + j)]


        # def backtrack(combo):
        #     print(combo, res)
        #     if len(combo) == k:
        #         return
        #     lower = combo[-1] if combo else 0
        #     for i in range(lower + 1, 10):
        #         temp = sum(combo) + i
        #         combo.append(i)
        #         backtrack(combo[:])
        #         else:
        #             continue
        # backtrack([])
        # return res