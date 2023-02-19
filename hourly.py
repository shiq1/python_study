#!/bin/env python3

#from sys import argv

#script, annual_salary = argv

annual_salary = int(input("What is your annual salary: "))

salary_weekly = float(annual_salary) / 52.0

hourly_pay = int(salary_weekly) / 40.0

bi_weekly_salary = 2 * salary_weekly

print(f"Here is your hourly pay: {hourly_pay}")

print(f"Here is your weekly salary {salary_weekly}")

print(f"Here is your biweekly salary {bi_weekly_salary}")
