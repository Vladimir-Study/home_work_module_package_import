from application import people, salary
from datetime import date

if __name__ == '__main__':
    print(date.today())
    people.get_employees()
    salary.calculate_salary()