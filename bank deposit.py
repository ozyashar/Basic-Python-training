# bank deposit
# deposit value - 1000
dValue = input('Please enter deposit value: ')
# percent per year - 3%
Percent = input('Please enter percent per year: ')
# number of years - 3
# This counter will stop after reaching 3 years.
count = 0
while int(dValue) > 0:
    dValue = int(dValue) * (1 + (int(Percent)/10))
    count += 1
    if count == 3:
        print("Result: ", int(dValue))
        break

else:
    print('Reached to end', dValue)