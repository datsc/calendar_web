"""

This code only works with the non-web version of the code.
To adapt it for the web version the travel dates in all three functions need to be adapted as well as the length in the assertion.

to run it, use:

   >> python -m unittest 
   
"""

import unittest
from single_travel import *

class TestsSingleTravel(unittest.TestCase):
  
    def test_single_travel_length_within(self):

        """
        Testing travel id=1  for between June-August 2023
        """
        
        current_travel = Travel(1).get_travel()
        travel_dates = Travel(1).get_dates()
        length = Travel(1).calculate_length(travel_dates, 
                                    datetime.datetime(2023,6,1),
                                    datetime.datetime(2023,8,2))
        self.assertEqual(length.days,10)

    def test_single_travel_length_start_outside(self):

        """
        Testing travel id=1  for between June-August 2023 starting after travel date
        """
        current_travel = Travel(1).get_travel()
        travel_dates = Travel(1).get_dates()
        length = Travel(1).calculate_length(travel_dates, 
                                                datetime.datetime(2023,7,23),
                                                datetime.datetime(2023,8,2))
        self.assertEqual(length.days,8)


    def test_single_travel_length_end_outside(self, travel_id=1):

        """
        Testing travel id=1  for between June-August 2023 starting after travel date
        """
        t=Travel(travel_id)
        current_travel = Travel(1).get_travel()
        travel_dates = Travel(1).get_dates()
        length = t.calculate_length(travel_dates, 
                                    datetime.datetime(2023,7,19),
                                    datetime.datetime(2023,7,28))
        self.assertEqual(length.days,8)


