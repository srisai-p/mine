import sys
def lonpalsub(inpu):
    A=inpu
    B=A[::-1]
    n=len(A)
    opt = [[0 for j in range(n+1)] for i in range(n+1)]
    pie = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (A[i-1]==B[j-1]):
                opt[i][j]=opt[i-1][j-1]+1
                pie[i][j]='d'
            elif (opt[i][j-1]>=opt[i-1][j]):
                opt[i][j]=opt[i][j-1]
                pie[i][j]='l'
            else:
                opt[i][j]=opt[i-1][j]
                pie[i][j]='u'
    num=opt[n][n]
    i=n
    j=n
    s=''
    while i>=0 and j>=0:
        if pie[i][j]=='d':
            s=A[i-1]+s
            i=i-1
            j=j-1
        elif pie[i][j]=='u':
            i=i-1
        else:
            j=j-1
    return(num,s)
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    else:
        x,y=lonpalsub(line)
        print(x)
        print(y)