def calculate_compound(monthly, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    months = years * 12

    balance = 0
    history = []

    for _ in range(months):
        balance = balance * (1 + monthly_rate) + monthly
        history.append(balance)

    return balance, history