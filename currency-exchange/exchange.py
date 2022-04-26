def exchange_money(budget, exchange_rate):
    return float(budget / exchange_rate)
def get_change(budget, exchanging_value):
    return budget - exchanging_value
def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills
    
def get_number_of_bills(budget, denomination):
    return int(budget / denomination)
def exchangeable_value(budget, exchange_rate, spread, denomination):
    real_rate = exchange_rate * (1 + spread / 100)
    new_curr = exchange_money(budget, real_rate)
    return new_curr - new_curr % denomination
    
def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    real_rate = exchange_rate * (1 + spread / 100)
    return int(exchange_money(budget, real_rate) - exchangeable_value(budget, exchange_rate, spread, denomination)) 
