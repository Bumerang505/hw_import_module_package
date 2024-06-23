from application.salary import calculate_salary
from application.db.people import get_employees
import datetime


today_date = datetime.date.today()

if __name__ == '__main__':
    print(f'Сегодня {today_date} и мы {calculate_salary()}')

if __name__ == '__main__':
    print(f'Сегодня {today_date} и мы {get_employees()}')
