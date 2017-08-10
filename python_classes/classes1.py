#! /usr/bin/env python

## from : https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/


class Customer(object):
	'''A customer of ABC Banck wuth a checking account. Customers have the
	following properties:

	Attributes:
		name: A string representing the customer's name
		balance: A float tracking the current balance of the customer's account.
	'''

	def __init__(self, name, balance=0.0) :
		'''Return a Costomer object whose name is *name* and starting
		balance is *balance*.'''

		self.name = name
		self.balance = balance

	def withdraw(self, amount):
		''' Return the balance afte withdrawing *amount* money units.'''
		if amount > self.balance:
			raise RuntimeError('Amount greater than available balance.')
		self.balance -=amount
		return(self.balance)

	def deposit(self, amount):
		'''Return the balance remaining after depositing *amount* money units.'''
		self.balance += amount
		return(self.balance)




class Car(object):

	# Static methods and attributes don't require any instance to work

	# STATIC ATTRIBUTE
	wheels = 4

	# STATIC METHOD
	@staticmethod
	def make_car_sound():
		print('VRooooooommmm')

	def __init__(self, make, model):
		self.make = make
		self.model = model



class Vehicule(object):

	@classmethod
	def is_motorcycle(cls):
		return cls.wheels == 2



## Customer object creation
jeff = Customer('Jeff Knupp', 1000.0)


## Car object creation

mustang = Car('Ford', 'Mustang')
#print(mustang.wheels)
#print(Car.wheels)
