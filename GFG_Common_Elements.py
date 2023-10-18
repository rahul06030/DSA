#User function Template for python3

'''
Given three arrays sorted in increasing order.
Find the elements that are common in all three arrays
i/p
6 5 8
1 5 10 20 40 80
6 7 20 80 100
3 4 15 20 30 70 80 120

o/p
20 80
'''
class Solution:
    def commonElements (self,a,b,c, n1, n2, n3):
        # your code here
        max_ab =max( max( max(a), max(b)), max(c))
        min_ab =min( min( min(a), min(b)), min(c))
        l=[0]*(max_ab+1)
        m=[0]
        if min_ab<0:
            m=[0]*(min_ab*-1+1)
        for i in set(a):
            if i<0:
                m[i*-1]+=1
            else:
                l[i]+=1
        for i in set(b):
            if i<0:
                m[i*-1]+=1
            else:
                l[i]+=1
        for i in set(c):
            if i<0:
                m[i*-1]+=1
            else:
                l[i]+=1
        ans=[-i for i in range(len(m)-1,-1,-1) if m[i]>=3]
        ans.extend([i for i in range(len(l)) if l[i]>=3])
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends