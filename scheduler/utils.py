# -*- coding: utf-8 -*-

# utils.py
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#
# Created..........2015-03-12
# Modified.........2015-03-12


"""This module contains any tools or utilities required by the scheduler
program.

"""


# Import required modules
import random


# Import required user made modules
from individual import Individual


def average(x):
    """This function calculates the average of a list of provided values.

    :param x: A list of values to be averaged.
    :type  x: List of Integers

    :return: The average of the provided list.

    """
    
    return sum(x) * 1.0 / len(x)
# end def average


def selection(population, size):
    """This function will perform a tournament selection from the given
    population. The tournament size must be provided.

    :param population: The population of individuals to select from.
    :type  population: List of Individual object

    :param size: The tournament selection size.
    :type  size: Integer

    :return: Best individual of the tournament.

    """

    # Initialize the randomizer each time this function is called
    random.seed()

    # Choose and initial best individual
    best = population[random.randint(0,len(population)-1)]

    # Lopp through entire tournament size and find the best individual
    for i in xrange(size):
        new = population[random.randint(0,len(population)-1)]
        if new.score < best.score:
            best = new

    return best
# end def selection


def crossover(mate_1, mate_2, employee_list, store, day):
    """This function will perform a crossover on two individuals to create a
    single child individual with a random selection of either parents genes.

    :param mate_1: Parent number one.
    :type  mate_1: Individual object

    :param mate_2: Parent number two.
    :type  mate_2: Individual object

    :param employee_list: List of all empolyees.
    :type  employee_list: List of Employee object

    :param store: The store that contains all store times.
    :type  store: Store object

    :param day: The current day being evaluated.
    :type  day: Integer

    :return: The new indivudal created from provided parents.

    """

    # Initialize the randomizer each time this function is called
    random.seed()
    
    # Define empty new chromosome for child
    new_c = []

    # Assign random genes from each parent
    for pos in xrange(len(mate_1.c)):
        new_c.append(random.choice([mate_1.c[pos], mate_2.c[pos]]))

    # Add mutation 5% of the time
    if random.randint(0,100) <= 5:
        new_c[random.randint(0,len(mate_1.c)-1)] = random.randint(0,len(employee_list)-1)

    # Create new individual from new chromosome
    child = Individual(new_c, employee_list, store, day)

    return child
# end def crossover
