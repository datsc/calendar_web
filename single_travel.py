import numpy as np
import datetime
import pandas as pd
from read_travels import my_calendar
from colorama import Fore,Style



class Travel:

    """
    This class gets information about a particular Travel given its id.
    It has beginning and end dates as well as length.
    """
    
    cal = my_calendar()
    whole_calendar = cal.read_file()
    
    def __init__(self, travel_no):#, from_loc, to_loc,from_date, to_date):

        self.travel_no=travel_no

    def get_travel(self):

        self.current_travel = self.whole_calendar[self.whole_calendar['Travel_ID']==self.travel_no]
        return self.current_travel

    def analyse_travel(self):
        
        self.current_travel = self.get_travel()

        self.number_of_steps = self.current_travel.shape[0]
        self.number_of_cities = np.unique(self.get_cities()).shape

        return(self.number_of_cities, self.number_of_steps,)

    def get_cities(self):
    
        self.current_travel = self.get_travel()
        self.cities = np.append(self.current_travel['From'].values,
                                        (self.current_travel['To'].values))
        return self.cities

    def get_dates(self):

        self.current_travel = self.get_travel()
        self.dates = self.current_travel['Date']#.values
        
        return self.dates
    

    def calculate_length(self, 
                         travel_dates,
                         year_start = datetime.datetime(2000,1,1) ,
                         year_end = datetime.datetime(2040,1,1)):
         
        """
        calculate away number of days if
            - the travel is fully within the boundary days
            - travel starts within boundary but ends after the boundary
            - travel starts before the boundary but ends within the boundary
            - travel is fully before or after the boundary

        """
        if (year_start<=pd.to_datetime(travel_dates.iloc[0])) & (
            year_end>=pd.to_datetime(travel_dates.iloc[-1])):
            print("""
            Travel is fully within range""")
            self.length = pd.to_datetime(travel_dates.iloc[-1]) - pd.to_datetime(travel_dates.iloc[0])
        elif (year_start>=pd.to_datetime(travel_dates.iloc[0])) & (
            year_start<=pd.to_datetime(travel_dates.iloc[-1])) & (
            year_end>=pd.to_datetime(travel_dates.iloc[-1])):
            print("""
            Travel starts within range but ends after""")
            self.length = pd.to_datetime(travel_dates.iloc[-1]) - year_start
        elif (year_end<=pd.to_datetime(travel_dates.iloc[-1])) & (
            year_end>=pd.to_datetime(travel_dates.iloc[0])) & ( 
            year_start<=pd.to_datetime(travel_dates.iloc[0])) :
            print("""
            travel starts before range but ends within""")
            self.length = year_end - pd.to_datetime(travel_dates.iloc[0]) 
        elif (year_end<=pd.to_datetime(travel_dates.iloc[0])) | (
            year_start>=pd.to_datetime(travel_dates.iloc[-1])) :
            print("""
            Travel is outside of the date range""")
            self.length = datetime.timedelta(days=0)
        return self.length+datetime.timedelta(days=1)
    

def run_single_travel(travel_id, range_start, range_end):
    current_travel = Travel(travel_id).get_travel()
    analysis = Travel(travel_id).analyse_travel()
    travel_dates = Travel(travel_id).get_dates()
    length = Travel(travel_id).calculate_length(travel_dates, 
                                                range_start,
                                                range_end)
    
    return travel_id, current_travel, analysis, travel_dates, range_start, range_end, length



if __name__=="__main__":


    print(f"""\n  
         **********************************************************************
          """)
    

    travel_id = int(input("travel_id="))

    travel_id, current_travel, analysis, travel_dates, range_start, range_end, length = run_single_travel(travel_id, range_start = datetime.datetime(2023,7,21),
                        range_end = datetime.datetime(2023,11,25))
    
    print("\n Traveling between", Fore.BLUE+f"{travel_dates.iloc[0].date()} and {travel_dates.iloc[-1].date()}")

    print(Style.RESET_ALL,f"""
    {current_travel[["Date","From","To","Travel_ID"]]}""")

    print(Fore.WHITE + 
    f""" \n\n If you want to change ranges please change the below in the """,Fore.RED+"""run_single_travel function
    """)

    print(Fore.WHITE+"range_start =", Fore.BLUE+f"{range_start.date()}"),
    print(Fore.WHITE+"range_end =", Fore.BLUE+f"{range_end.date()}")

    print(Fore.WHITE+"number of days within range = ", Fore.BLUE+f"{length.days}")
    print(Style.RESET_ALL)
