#! /usr/bin/env python

## from : https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/





class Car(object):
	'''
	A car for sale by Jeffcro Car Dealership

	Attributes:
		wheels: An integer representing the number of wheels the car has.
		miles: The integral number of miles driven on a car.
		make: The make of the car as a string.
		model: The model of the car as a string.
		year: The integral year the car was built.
		sold_on: the date the vehicule was sold.
	'''


	# STATIC METHOD
	@staticmethod
	def make_car_sound():
		print('VRooooooommmm')


	def __init__(self, wheels, miles, make, model, year, sold_on):
		'''Return a new Car object'''

		self.wheels = wheels
		self.miles = miles
		self.make = make
		self.model = model
		self.year = year
		self.sold_on = sold_on

	def sale_price(self):
		'''Return the sale price for this car as a float amount.'''
		if self.sold_on is not None:
			return(0.0)		# Already sold
		return(5000.0 * self.wheels)

	def purchase_price(self):
		'''Return the price for which we would pay to purchase the car.'''
		if self.sold_on is None:
			return(0.0)		# Not yet sold
		return(8000.0 - .10 * self.miles) 




class Vehicule(object):

	@classmethod
	def is_motorcycle(cls):
		return cls.wheels == 2




## Car object creation

mustang = Car('Ford', 'Mustang')
#print(mustang.wheels)
#print(Car.wheels)
