def compute_paye_taxation(salary, annual_pension_contributions=0.05):
    income_tax_payments = compute_income_tax(salary, annual_pension_contributions)
    ni_payments = compute_national_insurance(salary)
    student_loan_repayments = compute_student_loan_repayments(salary)

    total_tax_paid = income_tax_payments + ni_payments + student_loan_repayments
    
    return total_tax_paid

def compute_income_tax(salary, annual_pension_contributions=0.05, debug=False):
    taxable_income = salary * (1 - annual_pension_contributions)
    income_tax_payment = 0

    tax_free_allowance = 12_570

    # Tax free allowance deductions
    tax_free_allowance = 12_570
    income_over_100k = max(taxable_income - 100_000, 0)
    if income_over_100k > 0:
        deductable_from_tax_free_allowance = min(tax_free_allowance, income_over_100k/2)
        income_tax_payment = deductable_from_tax_free_allowance * 0.4

        if debug:
            print(f'Tax free income: {tax_free_allowance - deductable_from_tax_free_allowance}')
            print(f'Tax paid on deductions from tax free allowance: {income_tax_payment}')
    
    taxable_income_remaining = taxable_income - 12_570
    
    # Basic rate
    if taxable_income_remaining > 0:
        basic_rate = 0.2
        basic_rate_band_size = 50_270 - 12_570
        
        income_taxed_at_basic_rate = min(taxable_income_remaining, basic_rate_band_size)
        income_tax_payment = income_tax_payment + income_taxed_at_basic_rate * basic_rate
        taxable_income_remaining = max(taxable_income_remaining - basic_rate_band_size, 0)

        if debug:
            print(f'Tax paid from basic rate charges: {income_taxed_at_basic_rate*basic_rate}')
    
    # Higher rate
    if taxable_income_remaining > 0:
        higher_rate = 0.4
        higher_rate_band_size = 125_140 - 50_271
        
        income_taxed_at_higher_rate = min(taxable_income_remaining, higher_rate_band_size)
        income_tax_payment = income_tax_payment + income_taxed_at_higher_rate * higher_rate
        taxable_income_remaining = max(taxable_income_remaining - higher_rate_band_size, 0)

        if debug:
            print(f'Tax paid from higher rate charges: {income_taxed_at_higher_rate*higher_rate}')
    
    # Additional rate
    if taxable_income_remaining > 0:
        additional_rate = 0.45
        income_tax_payment = income_tax_payment + taxable_income_remaining * additional_rate

        if debug:
            print(f'Tax paid from additional rate charges: {taxable_income_remaining*additional_rate}')
    
    return income_tax_payment


def compute_national_insurance(salary, basic_rate=0.08):
    higher_rate = 0.02
    basic_rate_lower_bound = 1_048 * 12
    upper_rate_lower_bound = 4_189 * 12
    
    ni_payments = 0
    taxable_income_remaining = max(0, salary - basic_rate_lower_bound)
    
    # Basic rate
    if taxable_income_remaining > 0:
        basic_rate_band_size = upper_rate_lower_bound - basic_rate_lower_bound
        income_taxed_at_basic_rate = min(taxable_income_remaining, basic_rate_band_size)
        taxable_income_remaining = taxable_income_remaining - income_taxed_at_basic_rate
        ni_payments = ni_payments + income_taxed_at_basic_rate * basic_rate
    
    # Higher rate
    return ni_payments + taxable_income_remaining * higher_rate


def compute_student_loan_repayments(salary):
    salary_threshold = 27_295
    taxable_income = max(salary - salary_threshold, 0)
    return taxable_income*0.09
