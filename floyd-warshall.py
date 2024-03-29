#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
	    for i in range(0,len(matrix)):
	        for j in range(0,len(matrix)):
	            if matrix[i][j] == -1:
	                matrix[i][j] = 1e9
	            if i==j:
	                matrix[i][j] = 0
	    for k in range(0,len(matrix)):
	        for i in range(0,len(matrix)):
	            for j in range(0,len(matrix)):
	                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
	    for i in range(0,len(matrix)):
	        for j in range(0,len(matrix)):
	            if matrix[i][j] == 1e9:
	                matrix[i][j] = -1
		#Code here


#{ 
 # Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends
