#!/usr/bin/env python3
import sys
for arg in sys.argv[1:]:
    stat = arg.split(':')
    try:
    	JobNumber = int(stat[0])
    	Wage = int(stat[1])
    except:
    	print("Parameter Error")
    TaxableAmount = (Wage - 3500 - Wage*0.165)
    FiveInsuOneGold = (Wage*0.165)
    if (Wage <= 3500):
       SalaryAfterTax = '{:.2f}'.format(Wage - FiveInsuOneGold)
    if (0<TaxableAmount<=1500):
       SalaryAfterTax = '{:.2f}'.format(Wage - FiveInsuOneGold - TaxableAmount*0.03)
    if (1500 < TaxableAmount <= 4500):
       SalaryAfterTax = '{:.2f}'.format(Wage - FiveInsuOneGold - (TaxableAmount * 0.1 - 105))
    if (4500 < TaxableAmount <= 9000):
       SalaryAfterTax = '{:.2f}'.format(Wage - FiveInsuOneGold - (TaxableAmount * 0.2 - 555))
    if (9000 < TaxableAmount <= 35000):
       SalaryAfterTax = '{:.2f}'.format(Wage - FiveInsuOneGold - (TaxableAmount * 0.25 - 1005))
    if (35000 < TaxableAmount <= 55000):
       SalaryAfterTax = '{:.2f}'.format(Wage - FiveInsuOneGold - (TaxableAmount * 0.30 - 2755))
    if (55000 < TaxableAmount <= 80000):
       SalaryAfterTax = '{:.2f}'.format(Wage - FiveInsuOneGold - (TaxableAmount * 0.35 - 5505))
    if (TaxableAmount > 80000):
       SalaryAfterTax = '{:.2f}'.format(Wage - FiveInsuOneGold - (TaxableAmount * 0.45 - 13505))
    print(JobNumber, end=':')
    print(SalaryAfterTax)
