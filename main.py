from application import salary, people
from application.people import get_employees
from application.salary import calculate_salary
from datetime import datetime


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    current_datetime = datetime.now()
    print(current_datetime)

