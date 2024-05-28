# Travel Date Calculator

@Ugur Ural, 2024.

This code reads travel information from an Excel file and calculates the number of days one travelled within a range of dates. It is built for people who travel a lot for work and need to keep track of their travelling.

### EXAMPLE DATA

The input data can be added to the **travels.xlsx** which then need to be renamed Planning_travels.xlsx
- Date (the cell type is date in Excel and it is a datetime object in python.
- From and To are the cities one traveled between.
- Airlines (it is redundant for the moment).
- Travel ID corresponds to a single return trip. eg. If you traveled from Monaco to Mexico and then back, they both need to be labeled with the same ID, so that the code recognises this as a single trip of which it needs to calculate the length of.


### MODULES

- read_travels.py
- single_travel.py
  - Given trip id, it will calculate the length and will return details such as destination.
- general_calendar.py
  - It can calcuate the length of traveling between a range of dates. 
  - The dates can be adjusted in the __main__ section of the code.
- functional_code.
  - The overall calculator, for not it does the same with general_calendar.py but it will be extended to go through months of ranges automatically.
- test_single_travel.py only works for the non-web version. 

### USING THE CODE

- git clone ...
- python general_calendar.py


### DISCLAIMER

- It is possible that there are some bugs. Please feel free to reach out.
