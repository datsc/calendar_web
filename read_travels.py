import pandas as pd
import datetime


class my_calendar:

    """This class reads excel sheet and finds the current maximum travel id."""

    def __init__(self, file="./data/input/travels.xlsx"):
        self.file=file
        

    def read_file(self):
        self.out_df = pd.read_excel(self.file, 
                              sheet_name='Summary_Dates', 
                              header=0,
                              parse_dates=True)
        self.out_df = self.out_df[["Date","From","To","Travel_ID"]]
        self.out_df['Date'] = pd.to_datetime(self.out_df['Date'], format="%d%m%Y")
        return self.out_df
    
    def find_current_max_travel_id(self):
        out_df = self.read_file()
        self.max_id = out_df['Travel_ID'].max()
        return self.max_id
    
    def find_all_ids_within_daterange(self):
        pass


if __name__=="__main__":
    cal = my_calendar()
    whole_calendar = cal.read_file()
    print(whole_calendar)
