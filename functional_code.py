import datetime
from read_travels import my_calendar
from single_travel import Travel, run_single_travel
from colorama import Fore,Style
import pandas as pd
from general_calendar import GeneralCalendar, tests, run_single_range



option=1


if option==1:


    range_start, range_end, relevant_ids, full_length = run_single_range(
        range_start = datetime.datetime(2023,12,30), 
        range_end = datetime.datetime(2024,12,30))

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

    if full_length.days>=179:
        print(Fore.RED,f"""
              *****************************************
              DANGER ZONE: You are over the limit!!!!!!
              *****************************************
              """)

with open("outfile.txt","a") as f:
    
    current_string = str(''.join([f"""
        *************************************************************
        Between, {range_start.date()} and {range_end.date()}\n
        In total {full_length.days} days \n
        *************************************************************"""]))
    f.write(current_string)
f.close()
