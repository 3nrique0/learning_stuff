#! /usr/bin/python


## data from wikipedia "barème impots France"



def taxL1(salaire):
	'''
	Calculate Level 1 of taxes
	'''
	





## SOME DATA TO TEST
salaire1 = 8000
salaire2 = 16800
salaire3 = 35000
salaire4 = 65000
salaire5 = 80000
salaire6 = 170000
salaire7 = 250000

## LIMITS BETWEEN THE SALARY LIMITS
lim1, lim2, lim3, lim4 = 9710, 26818, 71898, 152260 
per1, per2, per3, per4 = 0, 14, 30, 41, 45



wage = salaire1

if (wage - limit1) < 0:
	toPay = taxL1(wage)



