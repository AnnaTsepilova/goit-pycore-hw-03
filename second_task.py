import random

def get_numbers_ticket(minimum: int, maximum: int, quantity: int):
    """
    Function return quantity amount of randmized numbers list
    """
    numbers = []

    if minimum < 1:
        print("Error: Min less than 1")
        return numbers

    if maximum > 1000:
        print("Error: Max more than 1000")
        return numbers

    if maximum - minimum < quantity:
        print("Error: quantity lower that numbers range")
        return numbers

    ## Creating pool of numbers between minimum and maximum
    numbers_pool = list(range(minimum, maximum + 1))

    ## Fetching unique numbers from pool
    numbers = random.sample(numbers_pool, quantity)
    numbers.sort()

    return numbers

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
