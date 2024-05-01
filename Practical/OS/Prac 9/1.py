def fifo(istream, frames):
    temp = [-1] * frames
    flist = [[]  for i in range(frames)]
    pagefault = 0
    lastr = 0
    for i in istream:
        if i not in temp:
            pagefault += 1
            if -1 in temp:
                temp[temp.index(-1)] = i
            else:
                temp[lastr] = i
                lastr += 1
                if lastr >= frames:
                    lastr = 0
        for j, f in enumerate(flist):
            if temp[j] == -1:
                f.append("-")
            else:
                f.append(temp[j])
    print(f"Page Faults = {pagefault}")
    for i in flist:
        for j in i:
            print(f"{j} ", end ="")
        print("")

def optimal(istream, frames):
    temp = [-1] * frames
    flist = [[-1] for i in range(frames)]
    pagefault = 0
    for idx, page in enumerate(istream):
        if page not in temp:
            pagefault += 1
            if -1 in temp:
                temp[temp.index(-1)] = page
            else:
                max_future_index = max(((istream[idx:].index(p) if p in istream[idx:] else float('inf'), i) for i, p in enumerate(temp)))[1]
                temp[max_future_index] = page   
        for j, p in enumerate(flist):
            if temp[j] == -1:
                p.append("-")
            else:
                p.append(temp[j])
    print(f"Page Faults = {pagefault}")
    for i in flist:
        for j in i:
            print(f"{j} ", end ="")
        print("")


def lru(istream, frames):
    temp = [-1] * frames
    flist = [[] for _ in range(frames)]
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
        for i in range(frames):
            if i != index and temp[i] != -1:
                lru[i] += 1
        lru[index] = 0  
        print(lru)
        for j, f in enumerate(flist):
            if temp[j] == -1:
                f.append("-")
            else:
                f.append(temp[j])
    print(f"Page Faults : {pagefault}")
    for i in flist:
        for j in i:
            print(j, end=" ")
        print("")


# istream = list(map(int, input("Enter all the frames: ")))
# frames = int(input("Enter number of frames: "))
print("FIFO")
fifo([7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]  , 3)
print("OPTIMAL")
optimal([7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]  , 3)
print("LRU")
lru([7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]  , 3)