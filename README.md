# Employee Attendance & Payroll Calculator

Calculates monthly payroll for employees based on attendance data, applying an attendance penalty for excessive absences and flagging any employees with missing wage data.

## Features
- Calculates each employee's salary from days present × daily wage
- Applies a 10% penalty for employees absent more than 5 days
- Identifies the employee with the best attendance for the month
- Flags employees whose wage data is missing (instead of crashing)
- Generates a complete payroll report CSV
- Handles missing input files and invalid numeric data gracefully

## How to Run
```bash
python payroll_calculator.py
```

**Input files required** (same folder):
- `attendance.csv` — columns: `Employee_ID, Name, Days_Present, Days_Absent`
- `wages.csv` — columns: `Employee_ID, Daily_Wage`

**Output**: `payroll_report.csv` with columns `Employee_name, Working_days, Total_salary, Remarks`

## Concepts Used
- CSV reading/writing with `csv.DictReader` / `csv.DictWriter`
- Error handling (`try-except` for `ValueError`, `KeyError`, `FileNotFoundError`)
- Conditional business logic (attendance-based penalty calculation)
- Composite dictionary keys (tuple key) to avoid collisions when names repeat
