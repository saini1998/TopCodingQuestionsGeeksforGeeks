"""

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image.

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

Example 1:

Input: image = {{1,1,1},{1,1,0},{1,0,1}},
sr = 1, sc = 1, newColor = 2.
Output: {{2,2,2},{2,2,0},{2,0,1}}
Explanation: From the center of the image 
(with position (sr, sc) = (1, 1)), all 
pixels connected by a path of the same color
as the starting pixel are colored with the new 
color.Note the bottom corner is not colored 2, 
because it is not 4-directionally connected to 
the starting pixel.
 

Your Task:
You don't need to read or print anyhting. Your task is to complete the function floodFill() which takes image, sr, sc and newColor as input paramater and returns the image after flood filling.
 

Expected Time Compelxity: O(n*m)
Expected Space Complexity: O(n*m)
 

Constraints:
1 <= n <= m <= 100
0 <= pixel values <= 10
0 <= sr <= (n-1)
0 <= sc <= (m-1)

"""


"""
    Recursion
"""

class RecursionSolution:
    
    def floodFillUtil(self, image, x, y, p, n):
        R = len(image)
        C = len(image[0])
        if (x<0 or y<0 or x>=R or y>=C or image[x][y]!=p or image[x][y]==n):
            return
            
        image[x][y]=n
        self.floodFillUtil(image, x, y-1, p, n)
        self.floodFillUtil(image,x, y+1, p, n)
        self.floodFillUtil(image,x+1, y, p, n)
        self.floodFillUtil(image,x-1, y, p, n)
        
    def floodFill(self, image, sr, sc, newColor):
        prevColor = image[sr][sc]
        self.floodFillUtil(image, sr, sc, prevColor, newColor)
        return image

"""
    BFS
"""

class BreadthFirstSearchSolution:

    def isValid(self, screen, m, n, x, y, prevC, newC):
        if x<0 or x>= m or y<0 or y>= n or screen[x][y]!= prevC or screen[x][y]== newC:
            return False
        
        return True
        
    def floodFill(self, image, sr, sc, newColor):
        queue = []
        x = sr
        y = sc
        m = len(image)
        n = len(image[0])
        newC = newColor
        prevC = image[x][y]
        queue.append([x, y])
        image[x][y] = newC
        while queue:
            currPixel = queue.pop()
            posX = currPixel[0]
            posY = currPixel[1]
            if self.isValid(image, m, n, (posX + 1), posY, prevC, newC):
                image[posX + 1][posY] = newC
                queue.append([posX + 1, posY])
                
            if self.isValid(image, m, n, posX-1, posY, prevC, newC):
                image[posX-1][posY]= newC
                queue.append([posX-1, posY])
        
            if self.isValid(image, m, n,  posX, posY + 1,  prevC, newC):
                image[posX][posY + 1]= newC
                queue.append([posX, posY + 1])
        
            if self.isValid(image, m, n,  posX, posY-1,  prevC, newC):
                image[posX][posY-1]= newC
                queue.append([posX, posY-1])

        return image
		
	

"""
    Driver Code
"""

M = 3
N = 3

screen = [[1, 1 , 1], [1 ,1 ,0], [1 ,0 ,1]]

x = 1
y = 1
newC = 2

obj = RecursionSolution()
ans = obj.floodFill(screen, x, y, newC)

print("Recursion Solution")
for _ in ans:
    for __ in _:
        print(__, end = " ")
    print()

ob = BreadthFirstSearchSolution()
an = ob.floodFill(screen, x, y, newC)
print("BFS Solution")
for _ in an:
    for __ in _:
        print(__, end = " ")
    print()




