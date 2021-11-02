# season of year:
# winter season (12-2)
# spring season (3-5)
# summer season (6-8)
# autumn season (9-11)

# Please enter below the month you want to check (1-12)
season = input('Please enter a month: ')
if int(season) in (12, 1, 2):
    print("This is winter season")
elif int(season) in (3, 4, 5):
    print("This is spring season")
elif int(season) in (6, 7, 8):
    print("This is summer season")
elif int(season) in (9, 10, 11):
    print("This is autumn season")
else:
    print("something else")