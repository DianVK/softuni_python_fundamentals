country_names = input().split(", ")
capital_cities = input().split(", ")
country_information = {key: value for key, value in zip(country_names, capital_cities)}

[print(f"{country} -> {country_information[country]}") for country in country_information]

# country_names = input().split(", ")
# capital_cities = input().split(", ")
# countries = {}
#
# capital_counter = 0
# for country in country_names:
#     countries[country] = capital_cities[capital_counter]
#     capital_counter += 1
#
# for current_country, capital in countries.items():
#     print(f"{current_country} -> {capital}")
