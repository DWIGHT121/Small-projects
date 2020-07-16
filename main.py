#get the age of user in days asking the date of birth
from datetime import datetime

Year = int(input("Enter your date of birth:Year"))
Month = int(input("Enter your month of birth"))
Date = int(input("Enter your date"))

#calling function to check if the year is leap year 

days = 0

def leapyearcheck(Year):
    if(Year%4==0 and Year%100!=0):
        if(Year%400==0):
            return 1

    else:
	    return 2



#leap year days till the end of the year
var1 = leapyearcheck(Year)
if var1 == 1:
    if Month == 2:
        days = 28-Date
        for month_days in range(3,12):
            if month_days%2==0:
                days +=30
            else:
                days+=31
    elif month == 1:
        days = 31-Date
        days = days+28
        for month_days2 in range(Month,12):
            if month_days2%2==0:
                days +=30
            else:
                days+=31
    else:
        if Month%2==0:
            days = 31-Date
        else:
            days = 30-Date
        for month_days3 in range(Month,12):
            if month_days3%2==0:
                days +=30
            else:
                days+=31

#non leap year days till the end of the year
else:
    if Month == 2:
        days = 29-Date
        for month_days in range(3,12):
            if month_days%2==0:
                days +=30
            else:
                days+=31
    elif Month == 1:
        days = 31-Date
        days = days+29
        for month_days4 in range(3,12):
            if month_days4%2==0:
                days +=30
            else:
                days+=31

    else:
        for month_days5 in range(Month,12):
            if month_days5%2==0:
                days +=30
            else:
                days+=31


#total days year-wise excluding current year
for loop1 in range(Year+1, datetime.now().year-1):
    var2 = leapyearcheck(loop1)
    if var2 == 1:
        days+=366
    else:
         days+=365

#checking if current year is leap year
var3 = leapyearcheck(datetime.now().year)    
if var3 == 1:
    if datetime.now().month==2:
        days+= (31+datetime.now().day)

    elif datetime.now().month==1:
        days+=datetime.now().day

    else:
        days+=(31+28)
        #calculating days till previous month
        for month_loop6 in range(3, datetime.now().month-1):
            if month_loop6%2==0:
                    days +=30
            else:
                days+=31
        #calculating days till today in this month
        days += datetime.now().day
else:
    if datetime.now().month==2:
        days+= (31+datetime.now().day)

    elif datetime.now().month==1:
        days+=datetime.now().day

    else:
        days+=(31+29)
        for month_loop7 in range(3, datetime.now().month-1):
            if month_loop7%2==0:
                    days +=30
            else:
                days+=31
        days += datetime.now().day
    
print("The age in days is \n")
print(days)
   


