import datetime

year = int(input())
flag = ''
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
if(year % 400 == 0):
    flag = 'L'
elif(year % 4 == 0 and year % 100 != 0):
    flag = 'L'
else:
    flag = 'N'

#print(flag)

firstDay = datetime.datetime(year, 1, 1)
secondDay = datetime.datetime(year, 1, 2)
firstDay = firstDay.strftime("%A")
secondDay = secondDay.strftime("%A")

for day in days:
    if(flag == 'N'):
        if(day == firstDay):
            print(day + ' - 53')
        else:
            print(day + ' - 52')
    elif(flag == 'L'):
        if(day == firstDay or day == secondDay):
            print(day + ' - 53')
        else:
            print(day + ' - 52')
            
