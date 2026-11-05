# Employee Salary Calculator
# Project: PS No. 9
# Language: Python 3

# Function to calculate salary
def calculate_salary(basic_salary):

    # Calculate HRA and DA
    hra = basic_salary * 0.20
    da = basic_salary * 0.10

    # Calculate gross salary
    gross_salary = basic_salary + hra + da

    # Calculate PF
    pf = basic_salary * 0.12

    # Calculate tax according to gross salary
    if gross_salary <= 25000:
        tax_rate = 0.00
    elif gross_salary <= 50000:
        tax_rate = 0.05
    else:
        tax_rate = 0.10

    # Calculate tax and net salary
    tax = gross_salary * tax_rate
    net_salary = gross_salary - pf - tax

    # Return all salary details
    return hra, da, gross_salary, pf, tax, net_salary


# Function to print salary slip
def print_salary_slip(name, employee_id, basic_salary):

    # Get salary details
    hra, da, gross, pf, tax, net = calculate_salary(basic_salary)

    # Display employee salary slip
    print("\n" + "=" * 42)
    print("       EMPLOYEE SALARY SLIP")
    print("=" * 42)

    # Print employee details
    print(f"Employee Name : {name}")
    print(f"Employee ID   : {employee_id}")
    print(f"Basic Salary  : ₹{basic_salary:.2f}")

    # Print salary components
    print("-" * 42)
    print(f"HRA (20%)     : ₹{hra:.2f}")
    print(f"DA (10%)      : ₹{da:.2f}")
    print(f"Gross Salary  : ₹{gross:.2f}")
    print(f"PF (12%)      : ₹{pf:.2f}")
    print(f"Tax           : ₹{tax:.2f}")

    # Print final net salary
    print("-" * 42)
    print(f"NET SALARY    : ₹{net:.2f}")
    print("=" * 42)


# Main function
def main():

    # Display project heading
    print("EMPLOYEE SALARY CALCULATOR")
    print("--------------------------")

    try:
        # Input number of employees
        number_of_employees = int(input("Enter number of employees: "))

        # Check employee count
        if number_of_employees <= 0:
            print("Invalid number.")
            return

        # Loop for each employee
        for employee_number in range(1, number_of_employees + 1):

            # Input employee details
            print(f"\nEnter details for Employee {employee_number}:")
            name = input("Employee name: ").strip()
            employee_id = input("Employee ID: ").strip()

            # Check empty details
            if not name or not employee_id:
                print("Name and ID cannot be empty.")
                continue

            try:
                # Input basic salary
                basic_salary = float(input("Basic salary (₹): "))

            except ValueError:
                # Handle invalid salary input
                print("Invalid salary.")
                continue

            # Check positive salary
            if basic_salary <= 0:
                print("Enter a positive salary.")
                continue

            # Print employee salary slip
            print_salary_slip(name, employee_id, basic_salary)

    except ValueError:
        # Handle invalid employee count
        print("Please enter a whole number.")


# Program execution starts here
if __name__ == "__main__":
    main()
