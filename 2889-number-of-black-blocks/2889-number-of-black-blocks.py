class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:

        number_blocks = (m - 1) * (n - 1)

        res_dict = {}
        blocks_containing = 0
        #seen = []
        def modify_dict_logic(i , j, counter):
            if (i,j) in res_dict:
                res_dict[(i,j)] += 1
            else:
                #seen.append((i,j))
                counter += 1
                res_dict[(i, j)] = 1
            return counter

        res = [0, 0, 0, 0, 0]
        for i,j in coordinates:
            prev_i = i - 1 < m - 1 and i > 0
            prev_j = j - 1 < n - 1 and j > 0
            curr_i = i < m - 1
            curr_j = j < n - 1
            if curr_i and curr_j:
                #res_dict[(i,j)] += 1
                blocks_containing = modify_dict_logic(i, j, blocks_containing)
            if curr_i and prev_j:
                #res_dict[(1, j - 1)] += 1
                blocks_containing = modify_dict_logic(i, j -1, blocks_containing)
            if prev_i and curr_j:
                #res_dict[(i - 1,j)] += 1
                blocks_containing = modify_dict_logic(i-1, j, blocks_containing)
            if prev_i and prev_j:
                #res_dict[(i-1,j-1)] += 1
                blocks_containing = modify_dict_logic(i-1,j-1, blocks_containing)
        
        for r in res_dict:
            if res_dict[r] == 1:
                res[1] += 1
            elif res_dict[r] == 2:
                res[2] += 1
            elif res_dict[r] == 3:
                res[3] += 1
            else:
                res[4] += 1
        res[0] = number_blocks - blocks_containing
        return res
            