

def findLCS(str1, str2, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    length = dp[m][n]
    lcs = [''] * (length + 1)
    lcs[length] = ''
    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs[length - 1] = str1[i - 1]
            i -= 1
            j -= 1
            length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    print("Dynamic Programming Matrix:")
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                print("0\t", end='')
            else:
                print(dp[i][j], end=' ')
                if str1[i - 1] == str2[j - 1]:
                    print("↖ ", end='\t')
                elif dp[i - 1][j] >= dp[i][j - 1]:
                    print("↑ ", end='\t')
                else:
                    print("← ", end='\t')
        print()
    print("Length of Longest Common Subsequence:", dp[m][n])
    print("Longest Common Subsequence:", ''.join(lcs))


str1 = input("Enter the first sequence: ")
str2 = input("Enter the second sequence: ")
m = len(str1)
n = len(str2)
findLCS(str1, str2, m, n)



