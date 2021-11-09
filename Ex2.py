# divide list into two: even and odd numbers

i = 0

EvenList = []
OddList = []

while int(i) < 8:
    N = input("Enter a number: ")

    if int(N) % 2 == 0:
        EvenList.append(N)
    else:
        OddList.append(N)

    i += 1

print("EvenList: ", EvenList)
print("OddList: ", OddList)
