import csv

# --------------------------------------------------

best_employee = {}
complete_file = []
dict_to_add_all = {}
wages = {}

# --------------------------------------------------

try:
    with open("attendance.csv","r") as file:
        attendance = list(csv.DictReader(file))
except FileNotFoundError:
    print("File not found")
    attendance = []

# --------------------------------------------------

try:
    with open("wages.csv","r") as row:
        val = csv.DictReader(row)
        for i in val:
            wages[i["Employee_ID"]] = int(i["Daily_Wage"])
except FileNotFoundError:
    print("File not found")

# --------------------------------------------------

for lines in attendance:
    employee = lines["Name"]
    
    # ----------------------------------------
    
    try:
        Days_present = int(lines["Days_Present"])
    except ValueError:
        print("There is some value error")
        Days_present = 0
    
    # ----------------------------------------
    
    try:
        Days_absent = int(lines["Days_Absent"])
    except ValueError:
        print("There is some value error")
        Days_absent = 0
    
    employee_ID = lines["Employee_ID"]
    
    # ----------------------------------------
    
    try: 
        Daily_wage = wages[employee_ID]
        wage_missing = False
    except KeyError:
        print("Wage of ",employee,employee_ID,"not availbale")
        Daily_wage = 0
        wage_missing = True
    
    # ----------------------------------------
    
    best_employee[employee_ID,employee] = Days_present
    
    # ----------------------------------------
    
    if Days_absent > 5:
        salary_after_de = Days_present * Daily_wage
        Deduction = salary_after_de * 0.10
        salary = salary_after_de - Deduction
        remarks = "Attendance warning"
    
    else:
        salary = Days_present * Daily_wage
        remarks = "Good Attendance"
    
    # ----------------------------------------
    
    if wage_missing:
        remarks = "Wage data missing"
    
    # ----------------------------------------
    
    dict_to_add_all = {
        "Employee_name": employee,
        "Working_days": Days_present,
        "Total_salary": salary,
        "Remarks": remarks
    }
    complete_file.append(dict_to_add_all)

# --------------------------------------------------

most_present,per = max(best_employee,key=best_employee.get)
print("Best Employ of the month:  ",most_present,per)

# --------------------------------------------------

with open("payroll_report.csv","w",newline="") as new_file:
    header = ["Employee_name","Working_days","Total_salary","Remarks"]
    report = csv.DictWriter(new_file,fieldnames=header)
    report.writeheader()
    report.writerows(complete_file)

# --------------------------------------------------
