class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = set([tuple(i) for i in queens])
        x, y = king[0], king[1]
        res = []
        # search by col up
        for i_col in range(y - 1, -1, -1):
            if (pos := (x,  i_col)) in queens:
                res.append(list(pos))
                break
        # search by col down
        for i_col in range(y + 1, 8):
            if (pos := (x, i_col)) in queens:
                res.append(list(pos))
                break
        # search by row left
        for i_row in range(x - 1, -1, -1):
            if (pos := (i_row, y)) in queens:
                res.append(list(pos))
                break
        # search by row right
        for i_row in range(x + 1, 8):
            if (pos := (i_row, y)) in queens:
                res.append(list(pos))
                break
        # search left up
        i = 1
        while (new_x := (x - i)) >= 0 and (new_y := (y - i)) >= 0:
            if (pos := (new_x, new_y)) in queens:
                res.append(list(pos))
                break
            i += 1
        # search right up
        i = 1
        while (new_x := (x + i)) < 8 and (new_y := (y - i)) >= 0:
            if (pos := (new_x, new_y)) in queens:
                res.append(list(pos))
                break
            i += 1
        # search left down
        i = 1
        while (new_x := (x - i)) >= 0 and (new_y := (y + i)) < 8:
            if (pos := (new_x, new_y)) in queens:
                res.append(list(pos))
                break
            i += 1
        # search right down
        i = 1
        while (new_x := (x + i)) < 8 and (new_y := (y + i)) < 8:
            if (pos := (new_x, new_y)) in queens:
                res.append(list(pos))
                break
            i += 1
        return res
