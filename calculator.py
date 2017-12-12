#!/usr/bin/env python3
import sys
try:
    int(sys.argv[1])
except:
    print("Parameter Error")
Wage = int(sys.argv[1])
TaxableAmount = int(Wage - 3500)
if (Wage <= 3500):
    print(format(0.00, ".2f"))
if (Wage > 3500 and TaxableAmount <= 1500):
    print('{:.2f}'.format(TaxableAmount * 0.03))
if (1500 < TaxableAmount <= 4500):
    print('{:.2f}'.format(TaxableAmount * 0.1 - 105))
if (4500 < TaxableAmount <= 9000):
    print('{:.2f}'.format(TaxableAmount * 0.2 - 555))
if (9000 < TaxableAmount <= 35000):
    print('{:.2f}'.format(TaxableAmount * 0.25 - 1005))
if (35000 < TaxableAmount <= 55000):
    print('{:.2f}'.format(TaxableAmount * 0.30 - 2755))
if (55000 < TaxableAmount <= 80000):
    print('{:.2f}'.format(TaxableAmount * 0.35 - 5505))
if (TaxableAmount > 80000):
    print('{:.2f}'.format(TaxableAmount * 0.45 - 13505))
