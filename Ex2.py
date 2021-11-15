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

print("EvenList: ", EvenList)
print("OddList: ", OddList)


