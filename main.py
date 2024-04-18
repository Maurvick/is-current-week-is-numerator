from datetime import date

def main():
    month = date.today().strftime("%m")
    year = date.today().strftime("%y")
    day = date.today().strftime("%d")
    dayname = getDay(year, month)
    # print(dayname)
    if (checkWeek(dayname, day)):
        print("numerator")
    else: 
        print("denominator")

def getDay(year, month):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    first_day_of_the_month = date(int(year), int(month), 1).weekday()
    return days[first_day_of_the_month]

def checkWeek(dayname, day):
    is_numerator = True
    days = int(day)
    if (dayname != "Monday"): 
        is_numerator = False
    # for i in range(0, days):
    #     if (i >= 7):
    #         is_numerator = not is_numerator
    #         if (days < 0):
    #             days = -days
    #         days = 7 - days 
    #         i = 0
    weeks = float(days / 7) 
    if (weeks % 2 != 0):
        return not is_numerator
    else:
        return is_numerator

if __name__ == '__main__':
    main()