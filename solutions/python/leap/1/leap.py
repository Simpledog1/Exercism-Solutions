def leap_year(year):
    year_leap = False
    if year % 4 == 0:
        year_leap = True
        if year % 100 == 0: 
            year_leap = False
            if year % 400 == 0:
                year_leap = True
    return year_leap
        
