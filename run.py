# -*- coding: utf-8 -*-

# run.py
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#
# Created..........2015-03-12
# Modified.........2015-03-12


# Import required modules
import random


# Import required user made modules
from scheduler import Store, Employee, Individual

common_grounds = Store()
employee_list  = []

employee_list.append(Employee(common_grounds, 'Tom'))
employee_list.append(Employee(common_grounds, 'Adam'))
employee_list.append(Employee(common_grounds, 'Julie'))
employee_list.append(Employee(common_grounds, 'Vini'))

employee_list[0].add_hours(0, '07:30', '12:00', common_grounds)
employee_list[0].add_hours(0, '14:00', '15:00', common_grounds)
employee_list[0].add_hours(1, '07:30', '12:30', common_grounds)
employee_list[0].add_hours(2, '07:30', '12:00', common_grounds)
employee_list[0].add_hours(3, '07:30', '12:30', common_grounds)
employee_list[0].add_hours(4, '07:30', '12:00', common_grounds)

employee_list[1].add_hours(0, '09:00', '09:30', common_grounds)
employee_list[1].add_hours(0, '11:00', '11:30', common_grounds)
employee_list[1].add_hours(0, '19:00', '21:30', common_grounds)
employee_list[1].add_hours(1, '07:30', '15:30', common_grounds)
employee_list[1].add_hours(2, '09:00', '09:30', common_grounds)
employee_list[1].add_hours(2, '11:00', '11:30', common_grounds)
employee_list[1].add_hours(2, '19:00', '21:30', common_grounds)
employee_list[1].add_hours(3, '07:30', '15:30', common_grounds)
employee_list[1].add_hours(4, '09:00', '09:30', common_grounds)
employee_list[1].add_hours(4, '11:00', '11:30', common_grounds)

employee_list[2].add_hours(0, '07:30', '21:30', common_grounds)
employee_list[2].add_hours(1, '07:30', '21:30', common_grounds)
employee_list[2].add_hours(2, '07:30', '21:30', common_grounds)
employee_list[2].add_hours(3, '16:00', '21:30', common_grounds)
employee_list[2].add_hours(4, '16:00', '18:30', common_grounds)
employee_list[2].add_hours(5, '10:00', '17:30', common_grounds)

employee_list[3].add_hours(0, '16:00', '21:30', common_grounds)
employee_list[3].add_hours(1, '16:00', '21:30', common_grounds)
employee_list[3].add_hours(2, '16:00', '21:30', common_grounds)
employee_list[3].add_hours(3, '07:30', '21:30', common_grounds)
employee_list[3].add_hours(4, '07:30', '18:30', common_grounds)
employee_list[3].add_hours(5, '10:00', '17:30', common_grounds)


pop_size   = 500
population = [Individual(None, employee_list, common_grounds, 0) for x in xrange(pop_size)]


for x in xrange(100):
    best = scheduler.utils.selection(population, pop_size)
    if best.score <= 10.0:
        break
    print "Epoch:", x, "=", best.score

    new_pop = []

    if (x % 5) == 0:
        pop_size -= 20
    while len(new_pop) < pop_size:
        m1 = scheduler.utils.selection(population, 20)
        m2 = scheduler.utils.selection(population, 20)
        new_pop.append(utils.crossover(m1, m2, employee_list, common_grounds, 0))
    
    population = new_pop

print
print
best = scheduler.utils.selection(population, pop_size)
print best.score
for t in xrange(len(best.c)):
    print common_grounds.date[0][t], ":", employee_list[best.c[t]].name
