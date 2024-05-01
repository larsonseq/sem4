def FCFS(NIOR, CY, THM, SCY):
   sum = 0.0
   for i in range(1, NIOR + 1):
       THM[i] = abs(CY[i - 1] - CY[i])
       sum += THM[i]
   ST = sum / NIOR
   print("\n-------------------------------------")
   print("|I/O REQUEST\tTOTAL HEAD MOVEMENT|")
   print("-------------------------------------")
   for i in range(1, NIOR + 1):
       print(f"{CY[i]}\t\t{THM[i]}")
   print("-------------------------------------")
   print(f"AVERAGE SEEK TIME IS : {ST}")


def SSTF(NIOR, DCY, THM, SCY):
   sum = 0.0
   for i in range(1, NIOR + 1):
       for j in range(1, NIOR):
           if abs(DCY[j] - SCY) > abs(DCY[j + 1] - SCY):
               temp = DCY[j]
               DCY[j] = DCY[j + 1]
               DCY[j + 1] = temp
   for i in range(1, NIOR + 1):
       THM[i] = abs(DCY[i - 1] - DCY[i])
       sum += THM[i]
   ST = sum / NIOR
   print("\n-------------------------------------")
   print("|I/O REQUEST\tTOTAL HEAD MOVEMENT|")
   print("-------------------------------------")
   for i in range(1, NIOR + 1):
       print(f"{DCY[i]}\t\t{THM[i]}")
   print("-------------------------------------")
   print(f"AVERAGE SEEK TIME IS : {ST}")


def SCAN(NIOR, CY, THM, SCY, MCY):
   cl = 0
   cr = 0
   sum = 0
   LCY = []
   RCY = []
   DCY = []
   for i in range(1, NIOR + 1):
       if CY[i] <= SCY:
           LCY.append(CY[i])
           cl += 1
       else:
           RCY.append(CY[i])
           cr += 1
   LCY.append(0)
   RCY.append(MCY)
   cl += 1
   cr += 1
   LCY.sort(reverse=True)
   RCY.sort()
   ttotal = cl + cr
   for i in range(ttotal):
       if i < cl:
           DCY.append(LCY[i])
       else:
           DCY.append(RCY[i - cl])
   for i in range(ttotal):
       if i == 0:
           THM.append(abs(SCY - DCY[i]))
       else:
           THM.append(abs(DCY[i - 1] - DCY[i]))
   for i in range(ttotal):
       sum += THM[i]
   print("\n-------------------------------------")
   print("|I/O REQUEST\tTOTAL HEAD MOVEMENT|")
   print("-------------------------------------")
   for i in range(ttotal):
       print(f"{DCY[i]}\t\t{THM[i]}")
   print("-------------------------------------")
   ST = sum / NIOR
   print(f"AVERAGE SEEK TIME IS : {ST}")



def main():
   NIOR = int(input("Enter the Number of IO Request "))
   CY = [0] * 20
   THM = [0] * 20
   print("Enter the Cylinder No")
   for i in range(1, NIOR + 1):
       CY[i] = int(input())
   SCY = int(input("Enter the Starting Cylinder "))
   MCY = int(input("Enter the Maximum Cylinder "))
   CY[0] = SCY
   print("FCFS")
   FCFS(NIOR, CY, THM, SCY)
   print("\nSSTF")
   SSTF(NIOR, CY, THM, SCY)
   print("\nSCAN")
   SCAN(NIOR, CY, THM, SCY, MCY)

if __name__ == "__main__":
   main()

