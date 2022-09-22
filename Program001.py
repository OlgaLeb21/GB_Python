work_day = [1,2,3,4,5]
weekend = [6,7]
numb_day = int(input('Enter the number of the day: '))
if numb_day in weekend:
    print("It's a day off!")
if numb_day in work_day:
    print('Working day...(')
else:
    print('We have only 7 days a week')
