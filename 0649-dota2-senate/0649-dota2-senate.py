class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_positions = deque([])
        d_positions = deque([])
        for i, s in enumerate(senate):
            if s == 'R':
                r_positions.append(i)
            else:
                d_positions.append(i)

        next_position = len(senate)
        while r_positions and d_positions:
            r = r_positions.popleft()
            d = d_positions.popleft()
            if r < d:
                r_positions.append(next_position)
            else:
                d_positions.append(next_position)
            
            next_position += 1
        return 'Radiant' if r_positions else 'Dire'
        # # ban = remove senator from queue entirely
        # # victory = all remaining senators are same party
        # # only one queue, we dont add anything to the queue at all - WRONG - remove from queue as rights revoked and keep looping until victory announced or no one left
        # # split the string into blocks of Rs and Ds in order they appear
        # prev = senate[0]
        # to_add = senate[0]
        # q = deque([])
        # # find first block and add it to the end of q
        # # then skip the first appearance of opposite party

        # for char in senate[1: ]:
        #     if char == prev:
        #         to_add += char
        #         prev = char
        #     else:
        #         q.append(to_add)
        #         prev = char
        #         to_add = char

        # if to_add:
        #     q.append(to_add)
        # print(q)
        # prev = q.popleft()
        # q.append(prev)
        # same = 0
        # temp = len(q)
        # if temp == 0:
        #     return "Radiant" if prev[0] == 'R' else "Dire"

        # while same != temp - 1:
        #     print(prev, q)
        #     temp = len(q)
        #     for i in range(temp):
        #         curr = q.popleft()
        #         if prev[-1] == curr[-1]:
        #             q.append(curr)
        #             same += 1
        #         elif len(curr) > 1:
        #             q.append(curr[1: ])
        #             prev = copy.deepcopy(curr)
        #         else:
        #             prev = copy.deepcopy(curr)

        # return "Radiant" if prev[0] == 'R' else "Dire"
            
            
            

                
       