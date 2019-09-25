def income(state, gross_income):
    federal_tax = 0.1 * gross_income

    if state == 'state1':
        state_tax = 0.1 * gross_income
    elif state == 'state2':
        state_tax = 0.15 * gross_income
    elif state == 'state3':
        state_tax = 0.20 * gross_income
    elif state == 'state4':
        state_tax = 0.25 * gross_income
    net_income = gross_income - federal_tax - state_tax
    return  net_income


print(income('state4', 10000))



