def fifo(istream, frames):
    temp = [-1] * frames
    flist = [[] for i in range(frames)]
    pagefault = 0
    lastr = 0
    for page in istream:
        if page not in temp:
            pagefault += 1
            if -1 in temp:
                temp[temp.index(-1)] = page
            else:
                temp[lastr] = page
                lastr += 1
                if lastr >= frames:
                    lastr = 0
        for j, f in enumerate(flist):
            if temp[j] == -1:
                f.append("-")
            else: 
                f.append(temp[j])
    print(f"Page Faults: {pagefault}")
    for i in flist:
        for j in i:
            print(j, end = " ")
        print("")

def optimal(istream, frames):
    temp = [-1] * frames
    flist = [[] for i in range(frames)]
    pagefault = 0
    for idx, page in enumerate(istream):
        if page not in temp:
            pagefault += 1
            if -1 in temp:
                index = temp.index(-1)
                temp[index] = page
            else:
                maxdist = max(((istream[idx:].index(p) if p in istream[idx:] else float('inf')), i) for i, p in enumerate(temp))[1] 
                temp[maxdist] = page
        for j, f in enumerate(flist):
            if temp[j] == -1:
                f.append("-")
            else: 
                f.append(temp[j])
    print(f"Page Faults: {pagefault}")
    for i in flist:
        for j in i:
            print(j, end = " ")
        print("")

def lru(istream, frames):
    temp = [-1] * frames
    flist = [[] for i in range(frames)]
    pagefault = 0
    lru = [0] * frames
    for idx, page in enumerate(istream):
        if page not in temp:
            pagefault += 1
            if -1 in temp:
                index = temp.index(-1)
            else:
                index = lru.index(max(lru))
            temp[index] = page
        else:
            index = temp.index(page)
        for i in range(len(lru)):
            if index != i and temp[i] != -1:
                lru[i] += 1
        lru[index] = 0
        for j, f in enumerate(flist):
            if temp[j] == -1:
                f.append("-")
            else: 
                f.append(temp[j])
    print(f"Page Faults: {pagefault}")
    for i in flist:
        for j in i:
            print(j, end = " ")
        print("")

print("FIFO")
fifo( [1, 2, 3, 4, 1, 5, 6, 3, 7, 8, 7, 8, 9, 7, 8, 9, 5, 4, 5, 4, 2]   , 3)
print("OPTIMAL")
optimal( [1, 2, 3, 4, 1, 5, 6, 3, 7, 8, 7, 8, 9, 7, 8, 9, 5, 4, 5, 4, 2]   , 3)
print("LRU")
lru( [1, 2, 3, 4, 1, 5, 6, 3, 7, 8, 7, 8, 9, 7, 8, 9, 5, 4, 5, 4, 2]   , 3)