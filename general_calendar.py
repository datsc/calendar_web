import datetime
from read_travels import my_calendar
from single_travel import Travel, run_single_travel
from colorama import Fore,Style
import pandas as pd



class GeneralCalendar:

    cal = my_calendar()
    whole_calendar = cal.read_file()

    def __init__(self, single_date_interested_start, 
                 date_interested_end, 
                 date_interested_year_start,
                 start_date=datetime.datetime(2020,1,1), 
                 end_date=datetime.datetime(2030,12,1)):
        
        self.start_date = start_date
        self.end_date = end_date
        self.single_date_interested_start = single_date_interested_start
        self.date_interested_end = date_interested_end
        if date_interested_year_start==0:
            self.date_interested_year_start = date_interested_end-datetime.timedelta(days=365)
        else:
            self.date_interested_year_start = date_interested_year_start
    
    def get_travel_ids(self):
        self.ids = self.whole_calendar[self.whole_calendar['Date'].between(
            self.date_interested_year_start, self.date_interested_end)]['Travel_ID']
        print(f"""
              *****************************************
              *****************************************
              *****************************************

                FROM {self.date_interested_year_start.date()}
                TO {self.date_interested_end.date()}

              *****************************************
              *****************************************
              *****************************************
              """)
        return self.ids

    
    """def calculate_number_of_days(self):
        "wrong"
        self.nr_days = self.end_date, self.start_date
        self.nr_days_limited = self.date_interested_end - self.single_date_interested_start
        
        return self.nr_days_limited
       """ 

def run_single_range(range_start, range_end):

    full_length=datetime.timedelta(days=0)

    cal_of_current = GeneralCalendar(
            single_date_interested_start=datetime.datetime(2024,6,4),
            date_interested_year_start=range_start,
            date_interested_end=range_end)
    
    relevant_ids = set(cal_of_current.get_travel_ids())
    print('here', relevant_ids)
   
    count = 0
    for id in relevant_ids:
        travel_id, current_travel, analysis, travel_dates, range_start, range_end, length = run_single_travel(id, range_start, range_end)
        full_length = full_length + length
        
        print(f"""\n  
        **********************************************************************
        """)
        print(Style.RESET_ALL,"\n Traveling between", Fore.BLUE+f"{travel_dates.iloc[0].date()} and {travel_dates.iloc[-1].date()}")
    
        print(Style.RESET_ALL,f"""
        {current_travel[["Date","From","To","Travel_ID"]]}""")

        print(Fore.WHITE+"number of days for this travel = ", Fore.BLUE+f"{length.days}")
        print(Fore.WHITE+"number of all days within range = ", Fore.BLUE+f"{full_length.days}")

        
        if count==0:
            all_travels=current_travel
        else:
            all_travels=pd.concat([all_travels,current_travel])
        count+=1

    
    print(Style.RESET_ALL, f"""\n ********FULL DATA***********\n\n, {all_travels}""")

    return range_start, range_end, relevant_ids, full_length


def tests(range_start, range_end):

    if range_start == datetime.datetime(2023,7,15) and range_end == datetime.datetime(2023,9,23):

        try:
            assert(full_length.days==31)
        except:
            raise Exception("If you see this error you have a BUG! YOU SHOULD HAVE GOTTON 31 DAYS")

      
if __name__=="__main__":


    range_start, range_end, relevant_ids, full_length = run_single_range(
        range_start = datetime.datetime(2023,6,25), 
        range_end = datetime.datetime(2024,7,7))

    #tests(range_start, range_end)

    print("""
        *************************************************************
          """,
        """\n 
        Between""", Fore.MAGENTA, f"{range_start.date()}",Fore.WHITE,  "and", Fore.MAGENTA, f"{range_end.date()}\n",
        Style.RESET_ALL,f""" 
        IDs are {relevant_ids}\n""",
        """
        In total""", Fore.MAGENTA, f"{full_length.days}", Fore.WHITE, "days \n",
        """
        *************************************************************
          """)

 
    if full_length.days>=175:
        print(Fore.RED,f"""
              *****************************************
              ALMOST 6 MONTHS OF TRAVELLING THIS YEAR
              *****************************************
              """)