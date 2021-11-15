# divide list into two: even and odd numbers

i = 0

EvenList = []
OddList = []

<<<<<<< HEAD
while int(i) < 8:
    lst = input("Enter a number: ")
=======
while int(i) < 8: # todo: why 8? should be a list of arbitrary length
    N = input("Enter a number: ")
>>>>>>> 1287023b0f7c93f5f29c8dcaf018449e04d2caff

    if int(lst) % 2 == 0:
        EvenList.append(lst)
    else:
        OddList.append(lst)

    i += 1
# todo: another task. try to divide this task into two part. 1. input list, 2. divide into odd and even
print("EvenList: ", EvenList)
print("OddList: ", OddList)


