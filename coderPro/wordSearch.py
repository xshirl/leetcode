class Grid(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __wordSearchRight(self, index, word):
        for i in range(len(self.matrix[index])):
            if word[i] != self.matrix[index][i]:
                return False
        return True

    def __wordSearchBottom(self, index, word):
        for i in range(len(self.matrix)):
            if word[i] != self.matrix[i][index]:
                return False
        return True

    def wordSearch(self, word):
        for i in range(len(self.matrix)):
            if self.__wordSearchRight(i, word):
                return True
        for i in range(len(self.matrix[0])):
            if self.__wordSearchBottom(i, word):
                return True
        return False


matrix = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]


print(Grid(matrix).wordSearch("ABCCED"))
