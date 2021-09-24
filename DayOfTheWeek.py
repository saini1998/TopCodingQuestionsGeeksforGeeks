"""

Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100

"""

from datetime import date
import calendar

class Solution:
    def dayOfTheWeek(self, d: int, m: int, y: int) -> str:
    	return date(y,m,d).strftime("%A")

    def dayOfTheWeek1(self, day: int, month: int, year: int) -> str:
        prev_year = year - 1
        days = prev_year * 365 + prev_year // 4 - prev_year // 100 + prev_year // 400
        days += sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month - 1])
        days += day

        if month > 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            days += 1

        return ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][days % 7]

    def findDay(self, day, month, year):
        dayNumber = calendar.weekday(year, month, day)
        days =["Monday", "Tuesday", "Wednesday", "Thursday",
                            "Friday", "Saturday", "Sunday"]
        return (days[dayNumber])


print("sol 1: ", Solution().dayOfTheWeek(21, 11, 1998))
print("sol 2: ", Solution().dayOfTheWeek1(21, 11, 1998))
print("sol 3: ", Solution().findDay(21, 11, 1998))