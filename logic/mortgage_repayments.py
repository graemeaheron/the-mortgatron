def compute_monthly_mortgage_repayments(total_debt, total_years, interest_rate):
    total_repayments = total_years * 12
    interest_rate = interest_rate / 12
    numerator = interest_rate * (1 + interest_rate) ** total_repayments
    denominator = (1 + interest_rate) ** total_repayments - 1
    return total_debt * numerator / denominator
