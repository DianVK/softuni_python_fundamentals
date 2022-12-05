import re
date = input()
date_pattern = r"[\d]{2}([.|\-|//])[A-Za-z]{3}(\1)[\d]{4}"
check_dates = re.finditer(date_pattern, date)
valid_dates = []
for valid in check_dates:
    valid_dates.append(valid[0])

for item in valid_dates:
    spliter = item[2]
    day,month,year = item.split(f"{spliter}")
    print(f"Day: {day}, Month: {month}, Year: {year}")

# import re
# dates = input()
#
# correct_dates = r"([0-9][0-9][/][A-Z][a-z][a-z][/]\d{4}|[0-9][0-9][-][A-Z][a-z][a-z][-]\d{4}|[0-9][0-9][.][A-Z][a-z][a-z][.]\d{4})"
#
# matches = re.finditer(correct_dates, dates)
# results = []
# for match in matches:
#     results.append(match[0])
#
# for el in range(len(results)):
#     current_date = results[el]
#     for x in range(len(current_date)):
#         day = current_date[0] + current_date[1]
#         month = current_date[3] + current_date[4] + current_date[5]
#         year = current_date[7] + current_date[8] + current_date[9] + current_date[10]
#         print(f"Day: {day}, Month: {month}, Year: {year}")
#         break