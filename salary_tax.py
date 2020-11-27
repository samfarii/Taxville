#! usr/bin/env python3

# This is a tool for tax obligations as a contractor

salary = int(input("Input total salary amount: "))
# This is the gross salary

if salary < 18000:
    print(f''' The salary is less than the threshold,
    there's no tax payable on {salary}''')
elif salary in range(18201, 37001):
    tax = (salary - 18200) * 0.19
    print(f"Total tax obligation on a salary of {salary} is: {tax} ")
elif salary in range(37001, 90001):
    tax = 3572 + ((salary - 37000) * 0.325)
    print(f"Total tax obligation on a salary of {salary} is: {tax} ")
elif salary in range(90001, 180001):
    tax = 20797 + ((salary - 90000) * 0.37)
    print(f"Total tax obligation on a salary of {salary} is: {tax} ")
else:
    tax = 54097 + ((salary - 180000) * 0.45)
    print(f"Total tax obligation on a salary of {salary} is: {tax} ")

yebo = (input("Do you want to see the monthly breakdown ?"))

if yebo in ['Y', 'y', 'yes', 'Yes'] :
    print("yeaaah")
else:
    print("Thanks for your time")
