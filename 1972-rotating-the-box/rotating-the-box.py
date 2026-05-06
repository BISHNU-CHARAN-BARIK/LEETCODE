class Solution(object):
    def rotateTheBox(self, boxGrid):
        m, n = len(boxGrid), len(boxGrid[0])
        for row in boxGrid:
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] == '*':
                    empty = j - 1
                elif row[j] == '#':
                    row[j], row[empty] = '.', '#'
                    empty -= 1

        rows = len(boxGrid)
        cols = len(boxGrid[0])

        t = []
        for j in range(cols):
            row = []
            for i in range(rows):
                row.append(boxGrid[i][j])
            t.append(row)

        for i in range(len(t)):
            t[i].reverse()

        return t