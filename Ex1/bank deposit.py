# bank deposit
# deposit value - 1000
dValue = input('Please enter deposit value: ')
# percent per year - 3%
Percent = input('Please enter percent per year: ')
Years = input('Please enter number of Years: ')

dValue = int(dValue)
Percent = int(Percent)
Years = int(Years)

# todo: number of years should be user input
count = 0
while dValue > 0:  # todo: no need to convert variable dValue to int every time
    dValue = dValue * (1 + (Percent / 10))
    count += 1
    if count == Years:
        print("Result: ", dValue)
        break
else:
    print('Please enter Deposit again with (+)', dValue)  # todo: statement is unreachable ()
