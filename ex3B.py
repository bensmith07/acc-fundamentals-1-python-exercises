# DEFINE VARIABLES

base_salary = 2000

commission_1 = .2
commission_2 = .15
commission_3 = .28
commission_4 = .35

bonus_1 = 0
bonus_2 = 1000
bonus_3 = 5000
bonus_4 = 100000

min_vacation_days = 3
vacation_pay_reduction = 200

min_longevity_months = 3

add_bonus_min_years = 5
add_bonus_min_sales = 100000
add_bonus = 1000

# GET USER INPUTS

name = input('Enter the salesperson\'s name: ')
longevity_months = int(input('Enter the total number of months the salesperson has been with the compnay: '))
longevity_years = int(input('Enter the total number of years the salesperson has been with the company: '))
vacation_days = int(input('Enter the number of vacation days taken this month: '))
monthly_sales = int(input('Enter the amount of sales made this month (to the nearest dollar): '))

# CALCULATE PAY

gross_pay = base_salary

# add commission
if monthly_sales > 1000000:
    gross_pay += (monthly_sales * commission_4)
elif monthly_sales > 500000:
    gross_pay += (monthly_sales * commission_3)
elif monthly_sales > 100000:
    gross_pay += (monthly_sales * commission_2)
elif monthly_sales >= 10000:
    gross_pay += (monthly_sales * commission_1)

# add bonus
if longevity_months >= min_longevity_months:
    if monthly_sales > 1000000:
        gross_pay += bonus_4
    elif monthly_sales > 500000:
        gross_pay += bonus_3
    elif monthly_sales > 100000:
        gross_pay += bonus_2
    elif monthly_sales >= 10000:
        gross_pay += bonus_1

# subtract vacation reduction
if vacation_days > min_vacation_days:
    gross_pay -= vacation_pay_reduction

# add additional bonus 
if (longevity_years >= add_bonus_min_years) and (monthly_sales > 100000):
    gross_pay += add_bonus
    
# DISPLAY OUTPUTS

# display basic info
print('Name of Salesperson: ', name)
print('Total Months of Service: ', longevity_months)
print('Total Years of Service: ', longevity_years)
print('Base Salary: ', '${:,.2f}'.format(base_salary))

# display commission amount
if monthly_sales > 1000000:
    print('Commission Earned: ', '${:,.2f}'.format(monthly_sales * commission_4))
elif monthly_sales > 500000:
    print('Commission Earned: ', '${:,.2f}'.format(monthly_sales * commission_3))
elif monthly_sales > 100000:
    print('Commission Earned: ', '${:,.2f}'.format(monthly_sales * commission_2))
elif monthly_sales >= 10000:
    print('Commission Earned: ', '${:,.2f}'.format(monthly_sales * commission_1))
else:
    print('Commission Earned: None')

# display bonus amount
if monthly_sales > 1000000:
    print('Bonus Earned: ', '${:,.2f}'.format(bonus_4))
elif monthly_sales > 500000:
    print('Bonus Earned: ', '${:,.2f}'.format(bonus_3))
elif monthly_sales > 100000:
    print('Bonus Earned: ', '${:,.2f}'.format(bonus_2))
elif monthly_sales >= 10000:
    print('Bonus Earned: ', '${:,.2f}'.format(bonus_1))
else:
    print('Bonus Earned: None')

# display additional bonus amount
if (longevity_years >= add_bonus_min_years) and (monthly_sales > 100000):
    print('Additional Bonus Earned: ', '${:,.2f}'.format(add_bonus))
else:
    print('Additional Bonus Earned: None')

# display vacation reduction amount
if vacation_days > min_vacation_days:
    print('Vacation Pay Reduction: ', '${:,.2f}'.format(vacation_pay_reduction))
else:
    print('Vacation Pay Reduction: None')

# display gross pay
print('Gross Pay: ', '${:,.2f}'.format(gross_pay))


# 
