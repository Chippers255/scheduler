# -*- coding: utf-8 -*-

# employee.py
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#
# Created..........2015-03-12
# Modified.........2015-03-12


class Employee (object):
	"""This class will represent an employee and there available time slots
	for each work day that the provided store is open.

	"""


	def __init__(self, store, name):
		"""

		"""

		self.date = []
		self.name = name

		self.date.append([True] * len(store.date[0]))
		self.date.append([True] * len(store.date[1]))
		self.date.append([True] * len(store.date[2]))
		self.date.append([True] * len(store.date[3]))
		self.date.append([True] * len(store.date[4]))
		self.date.append([True] * len(store.date[5]))
	# end def __init__


	def add_hours(self, date, t_start, t_end, store):
		"""

		"""

		for t in xrange(len(store.date[date])):
			if store.date[date][t] == t_start:
				start_time = t
			if store.date[date][t] == t_end:
				end_time = t

		for time in xrange(start_time, end_time+1):
			self.date[date][time] = False
	# end def add_hours


# end class Employee
