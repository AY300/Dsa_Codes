print("Enter First String")
s1=input()
l1=len(s1)
print("Enter second String")
s2=input()
l2=len(s2)

dp=[[-1 for i in range(l2+1)] for j in range(l1+1)]
def lcs(s1,s2,l1,l2,dp):
    if(dp[l1][l2]!=-1):
        return dp[l1][l2]
    elif(l1==0 or l2==0):
        return 0
    elif(s1[l1-1]==s2[l2-1]):
        dp[l1][l2]=1+lcs(s1,s2,l1-1,l2-1,dp)
    else:
        dp[l1][l2]=max(lcs(s1,s2,l1-1,l2,dp),lcs(s1,s2,l1,l2-1,dp))
    return dp[l1][l2]

print(lcs(s1,s2,l1,l2,dp))
print(dp)
for i in range(l1):
    print(dp[i])

def plcs(s1,s2,l1,l2,dp):
    res=""
    if(l1==0 or l2==0):
        return ""
    elif(s1[l1-1]==s2[l2-1]):
        res=plcs(s1,s2,l1-1,l2-1,dp)+s1[l1-1]
    elif(dp[l1][l2-1]>=dp[l1-1][l2]):
        res=plcs(s1,s2,l1,l2-1,dp)
    else:
        res=plcs(s1,s2,l1-1,l2,dp)
    return res
print(plcs(s1,s2,l1,l2,dp))
        
