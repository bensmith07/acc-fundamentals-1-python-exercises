
months_31 = [1, 3, 5, 7, 8, 10, 12]
months_30 = [4, 6, 9, 11]
months_28 = [2]

#Get date
print()
print('Input a date in the following format: mm/dd/yy.')
date = input('Date: ')

#Validate Month

month = int(date[:2])
while month not in range(1, 13):
  print()
  print('You must enter the date with a valid month.')
  print('Please try again.')
  print()
  date = input('Date: ')
  month = int(date[:2])

#Validate Day

day = int(date[3:5])
if month in months_31:
  while day not in range(1, 32):
    print()
    print('You must enter the date with a valid day 01 through 31.')
    print('Please try again.')
    print()
    date = input('Date: ')
    day = int(date[3:5])

if month in months_30:
  while day not in range(1, 31):
    print()
    print('You must enter the date with a valid day 01 through 30.')
    print('Please try again.')
    print()
    date = input('Date: ')
    day = int(date[3:5])

if month in months_28:
  while day not in range(1, 29):
    print()
    print('You must enter the date with a valid day 01 through 28.')
    print('Please try again.')
    print()
    date = input('Date: ')
    day = int(date[3:5])

#Validate Year 

year = date[6:]

while year != '13':
  print()
  print('The correct year is 2013 and must be entered as \'13\'.')
  print('Please try again.')
  print()
  date = input('Date: ')
  year = date[6:]

month = int(date[:2])
day = int(date[3:5])
year = int(date[-2:])

months_list = ['January', 'February', 'March', 'April', 'May',
               'June', 'July', 'August', 'September', 'October',
               'November', 'December']
print()
print('The date you entered is ',
      months_list[month - 1], ' ', day, ', 20', year, '.', sep='')








