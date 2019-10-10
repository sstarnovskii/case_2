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
print(annual_income)  # TODO: remove this "print" later
tax = 0
# Calculating tax value for each social status and annual revenue.
if social_status == 1:
    if annual_income <= 9075:
        tax = annual_income * 0.1
    if 9076 <= annual_income < 36900:
        tax = 9075 * 0.1 + (annual_income - 9075) * 0.15
    if 36901 <= annual_income < 89350:
        tax = 9075 * 0.1 + 36900 * 0.15 + (annual_income - 36900) * 0.25
    if 89351 <= annual_income < 186350:
        tax = 9075 * 0.1 + 36900 * 0.15 + 89350 * 0.25 + (annual_income - 89350) * 0.28
    if 186351 <= annual_income < 405100:
        tax = 9075 * 0.1 + 36900 * 0.15 + 89350 * 0.25 + 186350 * 0.28 + (annual_income - 186350) * 0.33
    if 405101 <= annual_income < 406750:
        tax = 9075 * 0.1 + 36900 * 0.15 + 89350 * 0.25 + 186350 * 0.28 + 405101 * 0.33 + (annual_income - 405100 * 0.35)
    if 406751 <= annual_income:
        tax = 9075 * 0.1 + 36900 * 0.15 + 89350 * 0.25 + 186350 * 0.28 + 405101 * 0.33 + 406750 * 0.35 + (annual_income - 406750) * 0.396
elif social_status == 2:
    if annual_income <= 18150:
        tax = annual_income * 0.1
    if 18151 <= annual_income < 73800:
        tax = 18150 * 0.1 + (annual_income - 18150) * 0.15
    if 73801 <= annual_income < 148850:
        tax = 18150 * 0.1 + 73800 * 0.15 + (annual_income - 73800) * 0.25
    if 148851 <= annual_income < 226850:
        tax = 18150 * 0.1 + 73800 * 0.15 + 148850 * 0.25 + (annual_income - 148850) * 0.28
    if 226851 <= annual_income < 405100:
        tax = 18150 * 0.1 + 73800 * 0.15 + 148850 * 0.25 + 226850 * 0.28 + (annual_income - 226850) * 0.33
    if 405101 <= annual_income < 457600:
        tax = 18150 * 0.1 + 73800 * 0.15 + 148850 * 0.25 + 226850 * 0.28 + 405100 * 0.33 + (annual_income - 405100 * 0.35)
    if 457601 <= annual_income:
        tax = 18150 * 0.1 + 73800 * 0.15 + 148850 * 0.25 + 226850 * 0.28 + 405100 * 0.33 + 457600 * 0.35 + (annual_income - 457600) * 0.396
else:
    print("For Nikita")
# TODO: copy 1 more time with column 3 stats for "else"

# TODO: make a nice data output (using local.py for phrases)
print(tax)
