def fifo(noir, cy, thm, scy):
    sum = 0.0
    for i in range(1, noir+1):
        thm[i] = abs(cy[i-1] - cy[i])
        sum += thm[i]
    st = sum / noir
    print("IO Request   THM")
    for i in range(1, noir+1):
        print(cy[i], "\t\t", thm[i])
    print(f"Average seek time is {st}")


def sstf(noir, cy, thm, scy):
    sum = 0.0 
    for i in range(1, noir + 1):
        for j in range(1, noir):
            if abs(cy[j] - scy) > abs(cy[j+1] -scy):
                temp = cy[j]
                cy[j] = cy[j+1]
                cy[j+1] = temp 
    for i in range(1, noir+1):
        thm[i] = abs(cy[i-1] - cy[i])
        sum += thm[i]
    st = sum / noir
    print("IO Request\tTHM")
    for i in range(1, noir+1):
        print(cy[i], "\t", thm[i])
    print(f"AVerage seek time is {st}")


def scan(noir, cy, thm, scy, mcy):
    cl = 0
    cr = 0
    sum = 0.0
    lcy = []
    rcy = []
    for i in range(1, noir+1):
        if cy[i] <= scy:
            lcy.append(cy[i])
            cl += 1
        else:
            rcy.append(cy[i])
            cr += 1
    lcy.append(0)
    rcy.append(mcy)
    cl += 1
    cr += 1
    lcy.sort(reverse=True)
    rcy.sort()
    total = cr + cl
    dcy = lcy + rcy
    print(rcy)
    print(lcy) 
    print(dcy)
    for i in range(total):
        if i == 0:
            thm.append(abs(scy - dcy[i]))
        else:
            thm.append(abs(dcy[i-1] - dcy[i]))
    print(thm)
    for i in range(total):
        sum += thm[i]
    for i in range(total):
       print(f"{dcy[i]}\t\t{thm[i]}")
    print(f"Average seek time is {sum/noir}")
    


noir = int(input("Enter Number of io requests: "))
cy = [0]
thm = [0] * (noir+1)
for i in range(1, noir + 1):
    cy.append(int(input("Enter cylinder no: ")))

scy = int(input("Enter starting cylinder: "))
mcy = int(input("Enter maximum cylinder: "))
cy[0] = scy
print("FIFO")
fifo(noir,cy.copy(), thm.copy(), scy)
print("SSTF:")
sstf(noir, cy.copy(), thm.copy(), scy)
print("SCAN:")
scan(noir, cy.copy(), [], scy, mcy)