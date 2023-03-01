#Problem 19
#Counting Sundays
"""Description(https://projecteuler.net/problem=19).
    You are given the following information, but you may prefer to do some research for yourself.
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

list_of_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def Counting_Sundays(first_date: tuple, last_date: tuple) -> int:
    """Calculate the number of all Sundays, wich felt on first day of the month on given period of time  
    
        Args: first and last dates in format (01, 01, 2000)
        Result: number of Sundays"""

    #days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    first_month_day = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    first_month_day_leap_year = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]
    days_in_years = []

    for year in range(first_date[2], last_date[2] + 1):#fill days_in_years
        if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
            days_in_years.append(366)
        else:
            days_in_years.append(365)
            
    number_of_sundays = 0
    for year in range(first_date[2], last_date[2] + 1):
        first_day = First_day_of_the_year(year)
        first_sunday = 1 + 7 - first_day
        if days_in_years[year - first_date[2]] == 365:
            for day in first_month_day:
                if (day - first_sunday) % 7 == 0:
                    number_of_sundays += 1
        else:
            for day in first_month_day_leap_year:
                if (day - first_sunday) % 7 == 0:
                    number_of_sundays += 1
    return number_of_sundays

def First_day_of_the_year(year:int) -> int:
    """Calculate first week day of the given year"""
    first_day = 1 #1Jan1900 - Monday
    days = 0
    
    if year > 1900:
        for i in range(1900, year):
            if (i % 4 == 0 and not i % 100 == 0) or i % 400 == 0:
                days += 366
            else:
                days += 365
        first_day = first_day + days % 7
    if year < 1900: return False #FIXME

    #print("first day of {} is {}".format(year, list_of_days[first_day - 1]))
    return first_day


def __main__():
    print(Counting_Sundays((1, 1, 1901), (1, 1, 2000)))


if __name__ == "__main__":
    __main__()

