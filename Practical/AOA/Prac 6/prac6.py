

def LCS(x, y):
    m = len(x)    #columns
    n = len(y)    #rows 
    global c
    global b
    b = [[0]*(n+1) for i in range(m+1)]
    c = [[0]*(n+1) for i in range(m+1)]
    for i in range(0,m+1):
        c[i][0] = 0 
    for j in range(0, n+1):
        c[0][j] = 0  
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = 'd'
            else:
                if c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    b[i][j] = 'u'
                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = 'l'

    print(" \t ", end=" ")
    print(" \t ", end=" ")
    for i in y:
        print(f"{i} \t", end = " ")
    print("")
    k = 0
    for i_row, l_row in zip(c, b):
        if k == 0:
            print("  \t", end =" ")
            k = 1
        else:
            print(f"{x[k-1]} \t", end=" ")
            k +=1
        for j, o in zip(i_row, l_row):
            print(f"{j} {o}\t", end=" ")
        print("")
    PrintLCS(b, x, len(x), len(y))

    
def PrintLCS(b, x, i, j):
    if j == 0 or i == 0:
        return 
    if b[i][j] == 'd':
        PrintLCS(b, x, i-1, j-1)
        print(x[i-1], end = "")
    elif b[i][j] == 'u':
        PrintLCS(b, x, i-1, j)
    else:
        PrintLCS(b, x, i, j-1)         


if __name__ == "__main__":
    str1 = input(f"Enter String 1: ")
    str2 = input(f"Enter String 2: ")
    LCS(str1, str2)