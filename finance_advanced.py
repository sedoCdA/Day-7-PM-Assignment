"""
Advanced Personal Finance Calculator.

Supports two-employee comparison and a financial health score.
"""


def get_float_input(prompt, min_val, max_val):
    """Prompt user for a float within a given range."""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"  Error: Enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("  Error: Please enter a valid number.")


def collect_employee(label):
    """Collect financial data for one employee."""
    print(f"\n  --- {label} ---")
    name = input("  Employee name          : ").strip()
    while not name:
        print("  Error: Name cannot be empty.")
        name = input("  Employee name          : ").strip()

    annual_salary = get_float_input("  Annual salary (₹)      : ", 0.01, 10_00_00_000)
    tax_rate = get_float_input("  Tax bracket (0-50%)    : ", 0, 50)
    monthly_rent = get_float_input("  Monthly rent (₹)       : ", 0.01, 10_00_00_000)
    savings_rate = get_float_input("  Savings goal (0-100%)  : ", 0, 100)

    return {
        "name": name,
        "annual_salary": annual_salary,
        "tax_rate": tax_rate,
        "monthly_rent": monthly_rent,
        "savings_rate": savings_rate,
    }


def calculate_finances(emp):
    """Calculate all financial figures for an employee dict."""
    monthly_gross = emp["annual_salary"] / 12
    monthly_tax = monthly_gross * (emp["tax_rate"] / 100)
    monthly_net = monthly_gross - monthly_tax
    rent_ratio = (emp["monthly_rent"] / monthly_net) * 100
    monthly_savings = monthly_net * (emp["savings_rate"] / 100)
    disposable = monthly_net - emp["monthly_rent"] - monthly_savings
    disposable_ratio = (disposable / monthly_net) * 100

    return {
        "monthly_gross": monthly_gross,
        "monthly_tax": monthly_tax,
        "monthly_net": monthly_net,
        "rent_ratio": rent_ratio,
        "monthly_savings": monthly_savings,
        "disposable": disposable,
        "disposable_ratio": disposable_ratio,
        "annual_tax": monthly_tax * 12,
        "annual_savings": monthly_savings * 12,
        "annual_rent": emp["monthly_rent"] * 12,
    }


def health_score(rent_ratio, savings_rate, disposable_ratio):
    """
    Calculate a financial health score from 0 to 100.

    Scoring formula:
      - Rent ratio  (40 pts): < 30% = 40, < 40% = 25, < 50% = 10, else 0
      - Savings rate (40 pts): >= 20% = 40, >= 10% = 25, >= 5% = 10, else 0
      - Disposable   (20 pts): >= 30% = 20, >= 15% = 10, else 0
    """
    rent_score = 40 if rent_ratio < 30 else (25 if rent_ratio < 40 else (10 if rent_ratio < 50 else 0))
    savings_score = 40 if savings_rate >= 20 else (25 if savings_rate >= 10 else (10 if savings_rate >= 5 else 0))
    disposable_score = 20 if disposable_ratio >= 30 else (10 if disposable_ratio >= 15 else 0)
    return rent_score + savings_score + disposable_score


def format_inr(amount):
    """Format a number in Indian Rupee lakhs/crores style."""
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
    return f"₹{'-' if is_negative else ''}{formatted}.{paise:02d}"


def score_label(score):
    """Return a text label for a given health score."""
    if score >= 80:
        return "Excellent 🟢"
    if score >= 60:
        return "Good 🟡"
    if score >= 40:
        return "Fair 🟠"
    return "Needs Attention 🔴"


def print_comparison(emp1, data1, emp2, data2):
    """Print a side-by-side comparison of two employees."""
    score1 = health_score(data1["rent_ratio"], emp1["savings_rate"], data1["disposable_ratio"])
    score2 = health_score(data2["rent_ratio"], emp2["savings_rate"], data2["disposable_ratio"])

    w = 20
    border = "═" * 62
    divider = "─" * 62

    print(f"\n{border}")
    print("           EMPLOYEE COMPARISON REPORT")
    print(border)
    print(f"  {'':25} {emp1['name']:<{w}} {emp2['name']:<{w}}")
    print(divider)
    print(f"  {'Annual Salary':<25} {format_inr(emp1['annual_salary']):<{w}} {format_inr(emp2['annual_salary']):<{w}}")
    print(f"  {'Monthly Gross':<25} {format_inr(data1['monthly_gross']):<{w}} {format_inr(data2['monthly_gross']):<{w}}")
    print(f"  {'Monthly Tax':<25} {format_inr(data1['monthly_tax']):<{w}} {format_inr(data2['monthly_tax']):<{w}}")
    print(f"  {'Monthly Net':<25} {format_inr(data1['monthly_net']):<{w}} {format_inr(data2['monthly_net']):<{w}}")
    print(f"  {'Rent':<25} {format_inr(emp1['monthly_rent']):<{w}} {format_inr(emp2['monthly_rent']):<{w}}")
    print(f"  {'Rent Ratio':<25} {data1['rent_ratio']:.1f}%{'':<{w-6}} {data2['rent_ratio']:.1f}%")
    print(f"  {'Monthly Savings':<25} {format_inr(data1['monthly_savings']):<{w}} {format_inr(data2['monthly_savings']):<{w}}")
    print(f"  {'Disposable':<25} {format_inr(data1['disposable']):<{w}} {format_inr(data2['disposable']):<{w}}")
    print(divider)
    print(f"  {'Health Score':<25} {score1}/100 — {score_label(score1):<{w}} {score2}/100 — {score_label(score2)}")
    print(f"{border}\n")


def main():
    """Entry point for two-employee comparison."""
    print("\n════ EMPLOYEE COMPARISON CALCULATOR ════")
    emp1 = collect_employee("Employee 1")
    emp2 = collect_employee("Employee 2")
    data1 = calculate_finances(emp1)
    data2 = calculate_finances(emp2)
    print_comparison(emp1, data1, emp2, data2)


if __name__ == "__main__":
    main()
