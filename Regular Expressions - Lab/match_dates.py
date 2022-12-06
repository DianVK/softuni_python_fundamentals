import re
dates = input()
date_pattern = r"\b\d{2}(?P<separator>[\.\-\/])[A-Za-z]{3}(?P=separator)\d{4}\b"
valid_dates = [obj.group() for obj in re.finditer(date_pattern,dates)]
for date in range(len(valid_dates)):
    current_date = valid_dates[date]
    current_day = current_date[0:2]
    current_month = current_date[3:6]
    current_year = current_date[7:11]
    print(f"Day: {current_day}, Month: {current_month}, Year: {current_year}")