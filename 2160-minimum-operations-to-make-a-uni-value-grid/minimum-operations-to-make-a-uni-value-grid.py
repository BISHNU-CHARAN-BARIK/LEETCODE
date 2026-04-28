class Solution(object):
    def minOperations(self, grid, x):
        flat = []
        for row in grid:
            flat.extend(row)
        rem = flat[0] % x
        if not all(i % x == rem for i in flat):
            return -1
        flat.sort()
        ind = len(flat) // 2
        total = 0
        for i in flat:
            total += abs(i - flat[ind]) // x

        return total