#! /usr/bin/env python

## from : https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/

from abc import ABCMeta, abstractmethod

class Vehicule(object):

	'''A vehicule for sale by Jeffco Car Dealership.

    Attributes:
        wheels: An integer representing the number of wheels the vehicule has.
        miles: The integral number of miles driven on the vehicule.
        make: The make of the vehicule as a string.
        model: The model of the Vehicule as a string.
        year: The integral year the vehicule was built.
        sold_on: The date the vehicule was sold.
    '''

	__metaclass__=ABCMeta

	base_sale_price = 0
	wheels = 0

	def __init__(self, miles, make, model, year, sold_on):
		self.miles = miles
		self.make = make
		self.model = model
		self.year = year
		self.sold_on = sold_on


	def sale_price(self):
		'''Return the sale price for this vehicule as a float amount.'''
		if self.sold_on is not None:
			return 0.0  # Already sold
		return(5000.0 * self.wheels)

	def purchase_price(self):
		'''Return the price for which we would pay to purchase the vehicule.'''
		if self.sold_on is None:
			return 0.0  # Not yet sold
		return(self.base_sale_price - (.10 * self.miles))

	@abstractmethod
	def vehicule_type():
		'''Return a string representing the type of vehicule this is.'''
		pass


class Car(Vehicule):

	def __init__(self, wheels, miles, make, model, year, sold_on):
		'''Return a new Car object'''

		base_sale_price = 8000
		wheels = 4

	def vehicule_type(self):
		return('car')



class Truck(Vehicule):

	def __init__(self, wheels, miles, make, model, year, sold_on):
		'''Return a new Car object'''

		base_sale_price = 10000
		wheels = 4

	def vehicule_type(self):
		return('truck')


class Motorcycle(Vehicule):
	'''A motorcycle for sale by Jeffco Car Dealership'''

	base_sale_price = 4000
	wheels = 2

	def vehicule_type(self):
		'''Return a string representing the type of vehicule this is'''
		return('motorcycle')
