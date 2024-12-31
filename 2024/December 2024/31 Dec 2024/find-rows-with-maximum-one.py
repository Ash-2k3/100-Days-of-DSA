class Solution:
    def rowWithMax1s(self, mat):
        current_maximum = 0
        index = -1

        for m in range(len(mat)):
            count = 0
            for n in range(len(mat[0])):
                if mat[m][n] == 1:
                    count += 1
            
            if current_maximum < count:
                current_maximum = count
                index = m

        return index