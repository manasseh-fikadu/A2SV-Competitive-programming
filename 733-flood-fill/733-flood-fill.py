class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(image,sr,sc,newColor):
            nonlocal sourceColor

            if sr<0 or sr>=len(image):
                return
            if sc<0 or sc>=len(image[0]):
                return 
            if image[sr][sc]!=sourceColor:
                return 

            image[sr][sc]=newColor

            dfs(image,sr-1,sc,newColor)
            dfs(image,sr,sc-1,newColor)
            dfs(image,sr,sc+1,newColor)
            dfs(image,sr+1,sc,newColor)


        sourceColor=image[sr][sc]
        if newColor==sourceColor:
            return image
        dfs(image,sr,sc,newColor)
        return image

            