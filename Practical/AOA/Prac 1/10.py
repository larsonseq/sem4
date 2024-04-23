import time 

def insertion(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j-1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -=1
        a[i+1] = key
    print (f"using insertion sort\n{a}\n")

def selection(a):
    for i in range(len(a)):
        j = i
        for k in range(i+1, len(a)):
            if a[k] < a[j]:
                j = k
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
    print(f"Using selection sort \n{a}\n")

a = list(map(int, input(f"Enter elements").split()))
t1 = time.time()
insertion(a.copy())

time.sleep(1)
t2 = time.time()
print(t2-t1)

t1 = time.time()
selection(a.copy())
time.sleep(1)
t2 = time.time()
print(t2-t1)

