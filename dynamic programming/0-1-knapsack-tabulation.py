#User function Template for python3
import sys
class Solution:
                
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp = [[0 for _ in range(0,W+1)] for _ in range(0,n)]
        if wt[0] <=  W:
            for i in range(wt[0],W+1):
                dp[0][i] = val[0]
                
                
        for i in range(1,n):
            for j in range(1,W+1):
                notTake = dp[i-1][j]
                take = 0
                if wt[i] <= j:
                    take = val[i]+dp[i-1][j-wt[i]]
                dp[i][j] = max(take,notTake)
        return dp[n-1][W]
       
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends
