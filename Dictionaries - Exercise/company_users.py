command = input()
company_databases = {}

while command != "End":
    company, employee_id = command.split(" -> ")
    if company not in company_databases:
        company_databases[company] = []
    if employee_id not in company_databases[company]:
        company_databases[company].append(employee_id)
    command = input()

for current_company in company_databases.items():
    company_name = current_company[0]
    print(company_name)
    company_employees = current_company[1]
    for employee in range(len(company_employees)):
        print(f"-- {company_employees[employee]}")
