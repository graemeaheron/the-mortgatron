from paye_taxation import compute_paye_taxation

def compute_income_after_paye(salary, pension_contributions_rate):
    paye_tax = compute_paye_taxation(salary, pension_contributions_rate)
    pension_contributions = salary * pension_contributions_rate
    return salary - paye_tax - pension_contributions


def compute_income_after_total_taxation(
    salary,
    pension_contributions_rate,
    annual_council_tax,
):
    post_paye_income = compute_income_after_paye(salary, pension_contributions_rate)
    return post_paye_income - annual_council_tax


def compute_income_after_essentials(
    salary,
    pension_contributions_rate,
    annual_council_tax,
    annual_home_insurance,
    annual_ground_rent,
    annual_service_charge,
    additional_living_costs
):
    post_tax_income = compute_income_after_total_taxation(salary, pension_contributions_rate, annual_council_tax)
    additional_costs = annual_home_insurance + annual_ground_rent + annual_service_charge + additional_living_costs
    return post_tax_income - additional_costs
