"""
Personal Finance Calculator.

Collects employee salary information and generates a financial breakdown
for an AI startup's employee benefits portal.
"""


def get_float_input(prompt, min_val, max_val):
    """Prompt user for a float input and validate it within a given range."""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"  Error: Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("  Error: Please enter a valid number.")


def collect_inputs():
    """Collect all employee financial inputs from the user."""
    print("\n  Enter employee details:")
    name = input("  Employee name          : ").strip()
    while not name:
        print("  Error: Name cannot be empty.")
        name = input("  Employee name          : ").strip()

    annual_salary = get_float_input(
        "  Annual salary (₹)      : ", 0.01, 10_00_00_000
    )
    tax_rate = get_float_input(
        "  Tax bracket (0-50%)    : ", 0, 50
    )
    monthly_rent = get_float_input(
        "  Monthly rent (₹)       : ", 0.01, 10_00_00_000
    )
    savings_rate = get_float_input(
        "  Savings goal (0-100%)  : ", 0, 100
    )

    return name, annual_salary, tax_rate, monthly_rent, savings_rate


def calculate_finances(annual_salary, tax_rate, monthly_rent, savings_rate):
    """Perform all financial calculations and return results as a dictionary."""
    monthly_gross = annual_salary / 12
    monthly_tax = monthly_gross * (tax_rate / 100)
    monthly_net = monthly_gross - monthly_tax
    rent_ratio = (monthly_rent / monthly_net) * 100
    monthly_savings = monthly_net * (savings_rate / 100)
    disposable = monthly_net - monthly_rent - monthly_savings

    annual_tax = monthly_tax * 12
    annual_savings = monthly_savings * 12
    annual_rent = monthly_rent * 12

    return {
        "monthly_gross": monthly_gross,
        "monthly_tax": monthly_tax,
        "monthly_net": monthly_net,
        "rent_ratio": rent_ratio,
        "monthly_savings": monthly_savings,
        "disposable": disposable,
        "annual_tax": annual_tax,
        "annual_savings": annual_savings,
        "annual_rent": annual_rent,
    }


def format_inr(amount):
    """Format a number in Indian Rupee style (lakhs/crores)."""
    amount = round(amount, 2)
    is_negative = amount < 0
    amount = abs(amount)

    rupees, paise = divmod(round(amount * 100), 100)
    rupees_str = str(rupees)

    if len(rupees_str) <= 3:
        formatted = rupees_str
    else:
        last_three = rupees_str[-3:]
        rest = rupees_str[:-3]
        groups = []
        while len(rest) > 2:
            groups.append(rest[-2:])
            rest = rest[:-2]
        if rest:
            groups.append(rest)
        groups.reverse()
        formatted = ",".join(groups) + "," + last_three

    result = f"₹{'-' if is_negative else ''}{formatted}.{paise:02d}"
    return result


def print_report(name, annual_salary, tax_rate, savings_rate, data):
    """Print the formatted financial summary report."""
    border = "═" * 44
    divider = "─" * 44

    print(f"\n{border}")
    print("       EMPLOYEE FINANCIAL SUMMARY")
    print(border)
    print(f" Employee      : {name}")
    print(f" Annual Salary : {format_inr(annual_salary)}")
    print(divider)
    print(" Monthly Breakdown:")
    print(f"   Gross Salary     : {format_inr(data['monthly_gross']):>16}")
    print(f"   Tax ({tax_rate:.1f}%)      : {format_inr(data['monthly_tax']):>16}")
    print(f"   Net Salary       : {format_inr(data['monthly_net']):>16}")
    print(
        f"   Rent             : {format_inr(data['monthly_rent'] if 'monthly_rent' in data else 0):>16}"
        f"  ({data['rent_ratio']:.1f}% of net)"
    )
    print(f"   Savings ({savings_rate:.1f}%)  : {format_inr(data['monthly_savings']):>16}")
    print(f"   Disposable       : {format_inr(data['disposable']):>16}")
    print(divider)
    print(" Annual Projection:")
    print(f"   Total Tax        : {format_inr(data['annual_tax']):>16}")
    print(f"   Total Savings    : {format_inr(data['annual_savings']):>16}")
    print(f"   Total Rent       : {format_inr(data['annual_rent']):>16}")
    print(f"{border}\n")


def main():
    """Entry point — collect inputs, calculate, and display the report."""
    name, annual_salary, tax_rate, monthly_rent, savings_rate = collect_inputs()
    data = calculate_finances(annual_salary, tax_rate, monthly_rent, savings_rate)
    data["monthly_rent"] = monthly_rent
    print_report(name, annual_salary, tax_rate, savings_rate, data)


if __name__ == "__main__":
    main()
