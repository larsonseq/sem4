def prefix(p):
    n = len(p)
    i = 0
    pie = [0]* len(p)
    for j in range(1, len(p)):
        while i > 0 and p[i] != p[j]:
            i = pie[i-1]
        if p[i] == p[j]:
            i += 1
        pie[j] = i
    return pie

def kmp(t, p):
    n =len(t)
    m = len(p)
    shifts = []
    pie = prefix(p)
    i = 0
    for j in range(0, n):
        while i > 0 and p[i] != t[j]:
            i = pie[i-1]
        if p[i] == t[j]:
            i += 1
        if i == m:
            shifts.append(j-m+1)
            i = pie[i-1]
    return shifts, pie

t = input("ENter text: ")
p = input("Enter pattern")
shifts, pie = kmp(t,p)
print(f"Prefix function is { pie}\n and shifts is {shifts}")