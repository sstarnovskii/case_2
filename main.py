# Case-study #2
# Developers:   Drachev Nikita (),
#               Starnovskiy Sergey (),
#               Zhuravlev Alexander ()
import local as lcl
social_status = int(input(lcl.STATUS))

# string constants

name_month = [lcl.JAN, lcl.FAB, lcl.MAR, lcl.APR, lcl.MAY, lcl.JUN, lcl.JUL, lcl.AUG, lcl.SEP, lcl.OCT, lcl.NOV, lcl.DEC]

annual_income = 0
for month in range(12):
    print('{} {} {}:'.format(lcl.QUESTION,name_month[month], lcl.CURRENCY, end =''))
    income = float(input())
    annual_income += income
print(annual_income)