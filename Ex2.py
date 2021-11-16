# divide list into two: even and odd numbers + Sum + Min + Max
i = 0
EvenList = []
OddList = []
sSum = int()
lMax = int()
lMin = int()
while int(i) < 8:
    lst = input("Enter a number: ")
    if int(lst) % 2 == 0:
        EvenList.append(lst)
    else:
        OddList.append(lst)
    i += 1
    sSum = sSum + int(lst)
    if int(lMax) < int(lst):
        lMax = lst
    if i == 0:
        lMin = lst
    else:
        if int(lMin) > int(lst):
            lMin = lst

# todo: another task. try to divide this task into two part. 1. input list, 2. divide into odd and even
print("EvenList: ", EvenList)
print("OddList: ", OddList)
print("Sum: ", sSum)
print("Min:", lMin, "Max:", lMax)
