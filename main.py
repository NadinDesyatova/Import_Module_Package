from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime


if __name__ == '__main__':
    data = datetime.date(datetime.today())
    employees = get_employees()
    salary = calculate_salary()
    print(f'{data}\n{employees}\n{salary}')
