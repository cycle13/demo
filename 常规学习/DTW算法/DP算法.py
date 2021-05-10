import numpy as np


def dp(world1,world2):
    m = len(world1)
    n = len(world2)
    dp = np.zeros(shape=(m+1,n+1))
    for i in range(1,m+1):
        dp[i][0] = dp[i-1][0]+1
    for i in range(1,n+1):
        dp[0][i] = dp[0][i-1]+1
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(world1[i-1] == world2[j-1]):
                dp[i][j] = dp[i-1][j-1]+(float(world1[i-1])-float(world2[j-1]))**2
            else:
                dp[i][j] = min(min(dp[i][j-1],dp[i-1][j]),dp[i-1][j-1])+(float(world1[i-1])-float(world2[j-1]))**2
    return (dp[m][n])



world1 = [1,1,1,10,2,3]
world2 = [1,1,1,2,10,3]
xl = dp(world1,world2)
print(xl)