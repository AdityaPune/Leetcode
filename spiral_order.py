class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        sr,sc = 0,0
        er,ec = len(matrix)-1, len(matrix[0])-1
        
        while sr<=er and sc<=ec:
            if sc==ec:
                for row in range(sr,er+1):
                    result.append(matrix[row][sc])
                break
            if sr==er:
                for col in range(sc,ec+1):
                    result.append(matrix[sr][col])
                break
            for col in range(sc,ec+1):
                result.append(matrix[sr][col])
                
            for row in range(sr+1,er+1):
                result.append(matrix[row][ec])
                
            for col in reversed(range(sc, ec)):
                result.append(matrix[er][col])
                
            for row in reversed(range(sr+1,er)):
                result.append(matrix[row][sc])
                
            sr+=1
            er-=1
            sc+=1            
            ec-=1
            
        return result
            