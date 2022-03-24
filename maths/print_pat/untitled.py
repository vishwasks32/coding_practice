def printPat(n):
    #Code here
    strng = ""
    for item in range(n,0,-1):
        for j in range(n,0,-1):
            strng += (str(j)+" ")*item
        strng+="$"
    return strng

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n= int(input())
        print (printPat(n))
        #printPat(n)
# } Driver Code Ends
