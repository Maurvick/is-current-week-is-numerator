from datetime import date

def main():
    month = date.today().strftime("%m")
    year = date.today().strftime("%y")
    day = date.today().strftime("%d")
    dayname = GetFirstDayOfTheWeek(year, month)
    if (checkWeek(dayname, day)):
        print("denominator")
    else: 
        print("numerator")

def GetFirstDayOfTheWeek(year, month):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    first_day_of_the_month = date(int(year), int(month), 1).weekday()
    return days[first_day_of_the_month]

def isMonthStartingFromMonday(dayname):
    if (dayname != "Monday"): 
        return False
    else:
        return True

def checkWeek(dayname, day):
    is_numerator = True
    days = int(day)
    weeks = float(days / 7) 
    if (weeks % 2 != 0):
        return not is_numerator
    else:
        return is_numerator

if __name__ == '__main__':
    main()
