import random

def get_numbers_ticket(min, max, quantity):
    list_of_tickets = []

    if (min >= 1 and ((min + quantity) <= max)) and max <= 1000:
        while len(list_of_tickets) < quantity:
            number = random.randint(min, max)
            list_of_tickets.append(number)

            d_list_of_tickets = set(list_of_tickets)
            list_of_tickets = list(d_list_of_tickets)

        sorted_list_of_tickets = sorted(list_of_tickets)
        return sorted_list_of_tickets
    
    return list_of_tickets
  

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
