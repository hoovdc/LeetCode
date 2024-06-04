#2373. Largest Local Values in a Matrix
#https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        input_size = len(grid) #just need one dimension bc grid is square. len(x)=len(y).
        #create grid to be returned, initially fill with zeros
        local_max_grid = [[0 for x in range(input_size-2)] for x in range(input_size-2)]
        #start one position in from edge and end one position in too
        for x_pos in range(1,input_size -1) :
            #same with the other dimension of the input grid
            for y_pos in range(1,input_size -1):
                 #find & store the max integer within the local grid
                 local_max_grid[x_pos-1][y_pos-1] = max(
                    grid[x_pos -1][y_pos-1], grid[x_pos -1][y_pos],grid[x_pos -1][y_pos+1],
                    grid[x_pos   ][y_pos-1], grid[x_pos   ][y_pos],grid[x_pos   ][y_pos+1],
                    grid[x_pos +1][y_pos-1], grid[x_pos +1][y_pos],grid[x_pos +1][y_pos+1])
        return local_max_grid

SolutionInstance = Solution()