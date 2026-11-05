# Employee Salary Calculator

**Project No.:** 9  
**Project Title:** Employee Salary Calculator  
**Language:** Python 3

## Project Overview
The Employee Salary Calculator is a console-based Python program that calculates an employee's gross and net salary from their basic salary. It computes HRA, DA, PF, and income tax, then displays a formatted salary slip.

## Objectives
- Practice Python functions, operators, conditional statements, and loops.
- Calculate salary components accurately using the given rules.
- Validate salary input and reject invalid/non-positive amounts.
- Support salary slips for multiple employees in one run.

## Features
- Accepts employee name, employee ID, and basic salary.
- Calculates HRA (20%), DA (10%), and PF (12%) of basic salary.
- Calculates tax based on gross salary:
  - Gross salary up to ₹25,000: 0%
  - Gross salary ₹25,001 to ₹50,000: 5%
  - Gross salary above ₹50,000: 10%
- Displays a formatted salary slip.
- Handles invalid numeric input and non-positive salaries.

## Requirements
- Python 3.8 or later (Python 3 recommended).
- No external packages or supporting data files are required.

## How to Run
1. Save the program as `one.py`.
2. Open a terminal in the folder containing the file.
3. Run:
   ```bash
   python one.py
   ```
   On some systems, use `python3 one.py`.
4. Enter the number of employees, then enter each employee's name, ID, and basic salary.

## Input Details
- Number of employees: positive whole number.
- Employee name: non-empty text.
- Employee ID: non-empty text.
- Basic salary: positive numeric value.

## Output Details
The salary slip displays:
- Employee name and ID
- Basic salary
- HRA, DA, gross salary, PF, tax, and net salary

## Formulae
- HRA = Basic Salary × 20%
- DA = Basic Salary × 10%
- Gross Salary = Basic Salary + HRA + DA
- PF = Basic Salary × 12%
- Net Salary = Gross Salary − PF − Tax

## Test Cases
| Case | Basic Salary | Expected Result |
|---|---:|---|
| 1. Normal input | ₹30,000 | Net salary ₹33,450 |
| 2. Boundary/minimum input | ₹10,000 | Net salary ₹11,800 |
| 3. Invalid input | −₹5,000 | Invalid salary message |
| 4. Different valid scenario | ₹50,000 | Net salary ₹52,500 |

## Project Files
- `one.py` — source code
- `README.md` — project documentation
- `Test_Cases.pdf` — test case input/output evidence

## Notes
The screenshots/PDF are prepared as sample console evidence for the four specified test cases. For final submission, run `one.py` on your own computer and replace or supplement them with screenshots captured from your actual execution if your instructor requires authentic desktop screenshots.
