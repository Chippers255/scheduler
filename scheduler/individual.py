# -*- coding: utf-8 -*-

# individual.py
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#
# Created..........2015-03-12
# Modified.........2015-03-12


# Import required modules
import math
import utils
import random


class Individual (object):
    """This class will represent a single individual in the population of
    schedules. An individual can be initialized randomly or defined with
    a set chromosome.

    """


    def __init__(self, c, employee_list, store, day):
        """This method will intialize an instance of the Individual class. An
        individual can be intialized randomly by passing None to the c value.
        A preset chromosome can be passed to c when creating a new child.

        :param c: A pre defined chromosome for the individual or None.
        :type  c: list of Integer or None

        :param employee_list: List of all empolyees.
        :type  employee_list: List of Employee object

        :param store: The store that contains all store times.
        :type  store: Store object

        :param day: The current day being evaluated.
        :type  day: Integer

        :return: None

        """

        # If no chromosome was provided then randomly generate one
        if c is None:
            # Intialize randomizer every time to avoid duplicates
            random.seed()
            self.c = [random.randint(0,len(employee_list)-1) for x in xrange(len(store.date[day]))]
        else:
            self.c = c

        self.score = 0

        # Evalute the individual at initialization
        self.evaluate(employee_list, store, day)
    # end def __init__


    def evaluate(self, employee_list, store, day):
        """The evaluation method uses 3 calculations to score a schedule.

        The t_score is the count of scheduling conflicts, this is when the
        scheduler schedules a person to work during a time they are not 
        available. This value will be weighted the most to ensure there are
        never any scheduling conflicts. This value is weighted and added to the
        total schedule score.

        The g_score is the count of each time an employee is scheduled for a
        shift that is shorter then 3hrs. This is import and will be weighted
        as we do not want the schedule to jump from person to person every hour
        or half hour. This value is summed up for each employee and then
        weighted, the weighted score is then added to the to schedule score.

        The e_score is the count of 30min sessions each employee is scheduled
        to work for that day. This value is the least important but we still
        want to create a fairly even schedule for employees. We calculate the
        standard deviation of each employees shceduled time and then add this
        to the total schedule score.

        :param employee_list: List of all empolyees.
        :type  employee_list: List of Employee object

        :param store: The store that contains all store times.
        :type  store: Store object

        :param day: The current day being evaluated.
        :type  day: Integer

        :return: None

        """

        # Number of schedule conflicts (Most important)
        self.t_score = 0

        # Number of 30min work sessions per employee
        self.g_score = [0] * len(employee_list)

        # Number of shifts < 3hr per employee
        self.e_Score = [0] * len(employee_list) 

        last_emp = 999
        last_len = 0
        for pos in xrange(len(self.c)):
            emp = self.c[pos]

            temp = employee_list[emp].date[day]
            if not temp[pos]:
                self.t_score += 1

            self.g_score[emp] += 1

            if last_emp != emp:
                if last_len < 6 and last_emp != 999:
                    self.e_Score[last_emp] += 1
                last_emp = emp
                last_len = 0

        # Schedule conflicts worth most weight
        self.score += self.t_score * 5

        # Number of shorts shifts is worth weight to enforce consistency
        self.score += sum(self.e_Score) * 2
 
        # STD of all employee shift time to ensure equality in scheduling
        avg = utils.average(self.g_score)
        variance = map(lambda x: (x - avg)**2, self.g_score)
        self.score += math.sqrt(utils.average(variance))
    # end def evaluate


# end class Individual
