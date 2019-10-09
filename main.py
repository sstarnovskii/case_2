# Case-study #2
# Developers:   Drachev Nikita (),
#               Starnovskiy Sergey (),
#               Zhuravlev Alexander ()
import local as lc

social_status = int(input(lc.STATUS))

name_month = [lc.JAN, lc.FAB, lc.MAR, lc.APR, lc.MAY, lc.JUN, lc.JUL, lc.AUG, lc.SEP, lc.OCT, lc.NOV, lc.DEC]

# Calculating annual income.
annual_income = 0
for month in range(12):
    print('{} {} {}:'.format(lc.QUESTION, name_month[month], lc.CURRENCY, end=''))
    income = float(input())
    annual_income += income
print(annual_income)
