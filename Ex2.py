# divide list into two: even and odd numbers

i = 0

EvenList = []
OddList = []


while int(i) < 8:
    lst = input("Enter a number: ")

    if int(lst) % 2 == 0:
        EvenList.append(lst)
    else:
        OddList.append(lst)

    i += 1
# todo: another task. try to divide this task into two part. 1. input list, 2. divide into odd and even
print("EvenList: ", EvenList)
print("OddList: ", OddList)


