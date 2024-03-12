from datetime import datetime

def get_days_from_today(date):
    try:
        date_format = "%Y-%m-%d"

        today = datetime.today()
        new_date = datetime.strptime(date, date_format)

        difference = new_date - today
        
        day = 'days' if abs(difference.days) > 1 else 'day'
        day = f'The difference with today is {difference.days} {day}'

        return print(day)
    except (TypeError, ValueError) as e:
        print(f'Sorry, an error occurred: {e}')


input = '2020-10-09'

get_days_from_today(input)