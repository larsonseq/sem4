def fcfs(noir, cy, scy):
    thm = []
    sum = 0.0
    for i in range(1, noir+1):
        thm.append(abs(cy[i] - cy[i-1]))
        sum += thm[i-1]
    st = sum / noir
    print("IO \t THM")
    for i in range(1, noir+1):
        print(f"{cy[i]} \t{thm[i-1]}")
    st = sum / noir
    print(f"Average seek time is {st}")

def sstf(noir, cy, scy):
    thm = [] 
    sum = 0.0
    for i in range(1, noir + 1):
        for j in range(1, noir):
            if abs(cy[j] - scy) > abs(cy[j+1] - scy):
                temp = cy[j]
                cy[j] = cy[j+1]
                cy[j+1] = temp
    for i in range(1, noir+1):
        thm.append(abs(cy[i] - cy[i-1]))
        sum += thm[i-1]
    st = sum / noir
    print(thm)
    print("IO \t THM")
    for i in range(1, noir+1):
        print(f"{cy[i]} \t{thm[i-1]}")
    st = sum / noir
    print(f"Average seek time is {st}")

def scan(noir, cy, scy, mcy):
    thm = []
    sum = 0.0
    rcy = []
    lcy = []
    rl = 0
    ll = 0
    for i in range(1, noir + 1):
        if cy[i] < scy:
            lcy.append(cy[i])
            ll += 1
        else:
            rcy.append(cy[i])
            rl += 1
    rcy.append(mcy)
    rl += 1
    lcy.append(0)
    ll += 1
    rcy.sort()
    lcy.sort(reverse=True)
    dcy = lcy + rcy
    print(dcy)
    total = ll + rl
    for i in range(total):
        if i == 0:
            thm.append(abs(dcy[i] - scy))
        else:
            thm.append(abs(dcy[i] - dcy[i-1]))  
    for i in thm:
        sum += i 
    st = sum / noir
    print(f"Average seek time is: {st}")
    for i in range(total):
        print(f"{dcy[i]} \t{thm[i]}")

cy = list(map(int, input("Enter Cylinders: ").split()))
noir = len(cy)
scy = int(input("Enter starting cylinder: "))
cy.insert(0, scy)
mcy = int(input("Enter maximum cylinder: "))

print("FCS:")
fcfs(noir, cy.copy(), scy)

print("SSTF")
sstf(noir, cy.copy(), scy)

print("SCAN: ")
scan(noir, cy.copy(), scy, mcy)